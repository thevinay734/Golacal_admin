import time

from pageObjects.dashboardPage import Dashboard
from selenium import webdriver
from pageObjects.loginPage import Login
from utilities.readProperties import ReadConfig

class Test_dashboard_view:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()

    def test_open_dashboard_view(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        time.sleep(3)
        login = Login(self.driver)
        login.setUserName(self.username)
        login.setPassword(self.password)
        login.clickLogin()
        time.sleep(3)

        dash_page = Dashboard(self.driver)
        dash_page.openDashboard()
        time.sleep(3)
        dash_page.openNewProvider()
        time.sleep(5)



