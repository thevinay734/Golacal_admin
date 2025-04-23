import time

import pytest
from selenium import webdriver
from pageObjects.loginPage import Login


class Test_001_login:
    def setup_method(self):
        self.baseUrl = "http://99.79.10.54:3000/admin/login"
        self.username = "golocal@gmail.com"
        self.password = "golocal@123"
        self.driver = webdriver.Chrome()

    def test_login(self):
        self.driver.get(self.baseUrl)
        time.sleep(10)
        self.lp = Login(self.driver)
        time.sleep(5)
        self.lp.setUserName(self.username)
        time.sleep(5)
        self.lp.setPassword(self.password)
        time.sleep(5)
        self.lp.clickLogin()
        time.sleep(5)
        self.lp.clickCategoryManage()
        time.sleep(3)









