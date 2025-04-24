import time

import pytest
from selenium import webdriver
from pageObjects.loginPage import Login


# class Test_001_login:
#     def setup_method(self):
#         self.baseUrl = "http://99.79.10.54:3000/admin/login"
#         self.username = "golocal@gmail.com"
#         self.password = "golocal@123"
#         self.driver = webdriver.Chrome()
#
#     def test_login(self):
#         self.driver.get(self.baseUrl)
#         time.sleep(10)
#         self.lp = Login(self.driver)
#         time.sleep(5)
#         self.lp.setUserName(self.username)
#         time.sleep(5)
#         self.lp.setPassword(self.password)
#         time.sleep(5)
#         self.lp.clickLogin()
#         time.sleep(5)
#         self.lp.clickCategoryManage()
#         time.sleep(3)

import pytest
import time
from pageObjects.loginPage import Login
from utilities.readProperties import ReadConfig

class Test_001_login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        time.sleep(3)
        login = Login(self.driver)
        time.sleep(3)
        login.setUserName(self.username)
        time.sleep(4)
        login.setPassword(self.password)
        time.sleep(3)
        login.clickLogin()
        time.sleep(5)
        login.clickLogOut()
        time.sleep(5)
        login.clickPopupOkButton()
        time.sleep(3)







