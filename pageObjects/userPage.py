from selenium.webdriver.common.by import By

class UserPage:
    menu_user_xpath = "//span[normalize-space()='User']"
    view_user_xpath = "//tbody/tr[1]/td[9]/div[1]/a[1]/button[1]"
    view_order_xpath = "//a[@class='btn btn-success']"

    def __init__(self, driver):
        self.driver = driver

    def openUserPage(self):
        self.driver.find_element(By.XPATH, self.menu_user_xpath).click()

    def clickFirstUserView(self):
        self.driver.find_element(By.XPATH, self.view_user_xpath).click()

    def clickUserOrderView(self):
        self.driver.find_element(By.XPATH, self.view_order_xpath).click()



