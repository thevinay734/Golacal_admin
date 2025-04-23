import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()  # Optional: maximizes browser window
    yield driver              # Return driver to test and quit after test
    driver.quit()
