from selenium.webdriver.common.by import By


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard = ''
        self.payment_history = ''
        self.profile_xpath = "//a[normalize-space()='Profile']"

    def click_profile_option(self):
        self.driver.find_element(By.XPATH, self.profile_xpath).click()
