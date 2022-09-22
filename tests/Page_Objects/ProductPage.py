from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.stocked_message_css_selector = ".text-green-500"
        self.non_stocked_message_css_selector = ".text-red-500"

    def get_stocked_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.stocked_message_css_selector).text

    def get_non_stocked_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.non_stocked_message_css_selector).text
