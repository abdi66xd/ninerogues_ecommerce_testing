from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, by_locator):
        self.wait.until(ec.presence_of_element_located(by_locator)).click()

    def send_keys(self, by_locator, value):
        # self.wait.until(ec.element_to_be_clickable(by_locator))
        self.wait.until(ec.presence_of_element_located(by_locator)).send_keys(value)

    def get_text(self, by_locator):
        return self.wait.until(ec.presence_of_element_located(by_locator)).get_attribute("innerText")

    def clear_field(self, by_locator):
        self.wait.until(ec.presence_of_element_located(by_locator)).clear()
