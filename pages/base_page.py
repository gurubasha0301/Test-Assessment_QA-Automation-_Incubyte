from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def visit(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator):
        element = self.find_element(locator)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
        element.click()

    def type(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

