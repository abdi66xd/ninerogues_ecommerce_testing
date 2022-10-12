from selenium.webdriver.common.by import By
from tests.Page_Objects.BasePage import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.first_name_field = (By.NAME, "first_name")
        self.last_name_field = (By.NAME, "last_name")
        self.email_field = (By.NAME, "email")
        self.password_field = (By.NAME, "password")
        self.re_password_field = (By.NAME, "re_password")
        self.register_button_xpath = (By.XPATH, "//button[normalize-space()='Register']")
        self.success_message = (By.CSS_SELECTOR, ".text-sm.font-medium.text-green-800")

    def enter_first_name(self, first_name):
        self.send_keys(self.first_name_field, first_name)

    def enter_last_name(self, last_name):
        self.send_keys(self.last_name_field, last_name)

    def enter_email(self, email):
        self.send_keys(self.email_field, email)

    def enter_password(self, password):
        self.send_keys(self.password_field, password)

    def enter_re_password(self, re_password):
        self.send_keys(self.re_password_field, re_password)

    def click_register_button(self):
        self.click(self.register_button_xpath)

    def get_message(self):
        self.get_text(self.success_message)
