from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ProviderPage:
    menu_provider_xpath = "//span[normalize-space()='Service Provider']"
    provider_view = "//body[1]/div[2]/div[1]/div[3]/div[2]/table[1]/tbody[1]/tr[1]/td[15]/div[1]/a[1]/button[1]"
    status_filter_name = "status"



    def __init__(self, driver):
        self.driver = driver

    def clickProvider(self):
        self.driver.find_element(By.XPATH, self.menu_provider_xpath).click()

    def clickProviderview(self):
        self.driver.find_element(By.XPATH, self.provider_view).click()

    def filterByStatus(self, value):
        select = Select(self.driver.find_element(By.NAME, self.status_filter_name))
        select.select_by_value(value)




