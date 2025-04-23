from selenium.webdriver.common.by import By

class Dashboard:
    menu_dashboard_xpath = "//span[normalize-space()='Dashboard']"

    def __init__(self, driver):
        self.driver = driver

    def openDashboard(self):
        self.driver.find_element(By.XPATH, self.menu_dashboard_xpath).click()