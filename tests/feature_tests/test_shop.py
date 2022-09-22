import time
import unittest
from selenium import webdriver

from tests.Page_Objects.HomePage import HomePage
from tests.Page_Objects.ProductPage import ProductPage
from tests.Page_Objects.ShopPage import ShopPage
from tests.feature_tests.constants import FRONTEND_URL

# Data set to test
stocked_product = "Shirt"
non_stocked_product = "Levi Black Cap"


class TestShop(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('D:/tutos/ninerogues_ecommerce/tests/drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_stocked_validation(self):
        driver = self.driver
        self.driver.get(FRONTEND_URL)
        home = HomePage(driver)
        home.click_shop_text()
        shop = ShopPage(driver)
        shop.choose_product(stocked_product)
        product = ProductPage(driver)
        stocked_message = product.get_stocked_message()
        time.sleep(3)
        self.assertEqual('In Stock', stocked_message)

    def test_non_stocked_validation(self):
        driver = self.driver
        self.driver.get(FRONTEND_URL)
        home = HomePage(driver)
        home.click_shop_text()
        shop = ShopPage(driver)
        shop.choose_product(non_stocked_product)
        product = ProductPage(driver)
        non_stocked_message = product.get_non_stocked_message()
        time.sleep(3)
        self.assertEqual('Out of Stock', non_stocked_message)

    @classmethod
    def tearDownClass(cls):
        cls.driver = cls.driver
        #cls.driver.close()
        #cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
