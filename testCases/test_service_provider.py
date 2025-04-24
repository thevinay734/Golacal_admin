import time
from pageObjects.loginPage import Login
from pageObjects.serviceProviderPage import ProviderPage
from utilities.readProperties import ReadConfig


class TestProvider:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()

    def test_provider_view(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        time.sleep(3)
        login = Login(self.driver)
        login.setUserName(self.username)
        login.setPassword(self.password)
        login.clickLogin()
        time.sleep(3)

        provider_page = ProviderPage(self.driver)
        provider_page.clickProvider()
        time.sleep(3)
        provider_page.clickProviderview()
        time.sleep(3)

    def test_filter_active_provider(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)

        login = Login(self.driver)
        login.setUserName(self.username)
        login.setPassword(self.password)
        login.clickLogin()
        time.sleep(3)

        provider_page = ProviderPage(self.driver)
        provider_page.clickProvider()
        time.sleep(2)

        provider_page.filterByStatus("true")  # Active
        time.sleep(3)
        # Optional: Add assertion based on filtered result

    def test_filter_inactive_provider(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)

        login = Login(self.driver)
        login.setUserName(self.username)
        login.setPassword(self.password)
        login.clickLogin()
        time.sleep(3)

        provider_page = ProviderPage(self.driver)
        provider_page.clickProvider()
        time.sleep(2)

        provider_page.filterByStatus("false")  # Inactive
        time.sleep(3)


        # Optional: Add assertion