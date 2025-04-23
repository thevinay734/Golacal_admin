import time
import pytest
from selenium import webdriver
from pageObjects.loginPage import Login
from pageObjects.userPage import UserPage
from utilities.readProperties import ReadConfig


class Test_UserPage:

    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()

    def test_open_order_user_view(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        time.sleep(3)
        login = Login(self.driver)
        login.setUserName(self.username)
        login.setPassword(self.password)
        login.clickLogin()
        time.sleep(3)

        user_page = UserPage(self.driver)
        user_page.openUserPage()
        time.sleep(3)
        user_page.clickFirstUserView()
        time.sleep(3)
        user_page.clickUserOrderView()
        time.sleep(3)



        # assert "user" in self.driver.current_url.lower()
        # def setup_method(self):
        #     self.baseUrl = "http://99.79.10.54:3000/admin/login"
        #     self.username = "golocal@gmail.com"
        #     self.password = "golocal@123"
        #     self.driver = webdriver.Chrome()

        # def test_open_user_page(self):
        #     self.driver.get(self.baseUrl)
        #     time.sleep(3)
        #     login = Login(self.driver)
        #     login.setUserName(self.username)
        #     login.setPassword(self.password)
        #     login.clickLogin()
        #     time.sleep(5)
        #
        #     user_page = UserPage(self.driver)
        #     user_page.openUserPage()
        #     time.sleep(3)
        #
        #     # Optionally assert something, e.g. URL or visible element
        #     assert "user" in self.driver.current_url.lower()

        # def teardown_method(self):
        #     self.driver.quit()

        # def test_open_user_view(self):
        #     self.driver.get(self.baseUrl)
        #     time.sleep(3)
        #     login = Login(self.driver)
        #     login.setUserName(self.username)
        #     login.setPassword(self.password)
        #     login.clickLogin()
        #     time.sleep(5)
        #
        #     user_page = UserPage(self.driver)
        #     user_page.openUserPage()
        #     time.sleep(3)
        #     user_page.clickFirstUserView()
        #     time.sleep(3)
        #
        #     # Optional: assert page title or URL to verify view page loaded
        #     assert "user" in self.driver.current_url.lower()

