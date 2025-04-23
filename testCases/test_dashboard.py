import time

from pageObjects.dashboardPage import Dashboard
from selenium import webdriver
from pageObjects.loginPage import Login



class Test_dashboard_view:

    def setup_method(self):
        self.baseUrl = "http://99.79.10.54:3000/admin/login"
        self.username = "golocal@gmail.com"
        self.password = "golocal@123"
        self.driver = webdriver.Chrome()

    def test_open_dashboard_view(self):
        self.driver.maximize_window()
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



