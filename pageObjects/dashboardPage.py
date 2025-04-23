from selenium.webdriver.common.by import By

class Dashboard:
    menu_dashboard_xpath = "//span[normalize-space()='Dashboard']"
    new_provider_css = "a[href='/admin/vender_view?id=792&keyword=edit']"

    def __init__(self, driver):
        self.driver = driver

    def openDashboard(self):
        self.driver.find_element(By.XPATH, self.menu_dashboard_xpath).click()

    def openNewProvider(self):
        self.driver.find_element(By.CSS_SELECTOR,self.new_provider_css).click()

