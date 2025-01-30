from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class RegistrationPage(BasePage):
    CREATE_ACCOUNT_LINK = (By.XPATH, "//div[@class='panel header']//a[.='Create an Account']")
    FIRST_NAME = (By.ID, "firstname")
    LAST_NAME = (By.ID, "lastname")
    EMAIL = (By.ID, "email_address")
    PASSWORD = (By.ID, "password")
    CONFIRM_PASSWORD = (By.ID, "password-confirmation")
    SUBMIT_BUTTON = (By.XPATH, "//button[@title='Create an Account']")

    def go_to_create_account(self):
        self.click(self.CREATE_ACCOUNT_LINK)

    def fill_registration_form(self, first_name, last_name, email, password):
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        self.type(self.CONFIRM_PASSWORD, password)

    def submit_form(self):
        self.click(self.SUBMIT_BUTTON)
    
    def type_with_delay(self, locator, text, delay=5):
        field = self.find_element(locator)
        for char in text:
            field.send_keys(char)
            time.sleep(delay)
