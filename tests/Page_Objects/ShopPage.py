import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.stocked_product_name_xpath = "//a[normalize-space()='Shirt']"
        self.non_stocked_product_name_xpath = "//a[normalize-space()='Levi Black Cap']"
        self.base_product_name = "//a[normalize-space()='{0}']"

    def choose_product(self, product_name):
        self.driver.find_element(By.XPATH, self.base_product_name.format(product_name)).click()

    def choose_stocked_product(self):
        self.driver.find_element(By.XPATH, self.stocked_product_name_xpath).click()

    def choose_non_stocked_product(self):
        self.driver.find_element(By.XPATH, self.non_stocked_product_name_xpath).click()
