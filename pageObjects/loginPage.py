from selenium.webdriver.common.by import By


class Login:
    textbox_username_id = "email"
    textbox_password_id = "password"
    button_login_xpath = "//button[normalize-space()='Login']"
    press_category = "//span[normalize-space()='Category Management']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickCategoryManage(self):
        self.driver.find_element(By.XPATH, self.press_category).click()