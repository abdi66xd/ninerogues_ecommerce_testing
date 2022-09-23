import time
import unittest
from selenium import webdriver

from tests.Page_Objects.CartPage import CartPage
from tests.Page_Objects.HomePage import HomePage
from tests.Page_Objects.LoginPage import LoginPage
from tests.Page_Objects.ProductPage import ProductPage
from tests.Page_Objects.ShopPage import ShopPage
from tests.feature_tests.constants import FRONTEND_URL

# Data set to test
user = "abdiasalpire12+25@gmail.com"
password = "7928003cba"
product_name = "Shirt"


class TestCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('D:/tutos/ninerogues_ecommerce/tests/drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_add_product(self):
        driver = self.driver
        self.driver.get(FRONTEND_URL+"login")
        time.sleep(2)
        login = LoginPage(self.driver)
        login.enter_username(user)
        login.enter_password(password)
        login.click_login_button()
        time.sleep(2)
        home = HomePage(self.driver)
        home.click_shop_text()
        time.sleep(2)
        shop = ShopPage(driver)
        shop.choose_product(product_name)
        time.sleep(2)
        product = ProductPage(self.driver)
        product.click_add_to_cart_button()
        time.sleep(2)
        cart = CartPage(self.driver)
        cart_total_items_message = cart.get_cart_items_message()
        time.sleep(2)
        self.assertEqual('Shopping Cart Items (1)', cart_total_items_message)

    def test_remove_product(self):
        driver = self.driver
        self.driver.get(FRONTEND_URL+"login")
        login = LoginPage(self.driver)
        login.enter_username(user)
        login.enter_password(password)
        login.click_login_button()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(4)
        home = HomePage(self.driver)
        home.click_cart_icon()
        cart = CartPage(self.driver)
        # Only clear the cart once time
        cart.click_x_icon()
        time.sleep(2)
        cart_total_items_message = cart.get_cart_items_message()
        self.assertEqual('Shopping Cart Items (0)', cart_total_items_message)

    @classmethod
    def tearDownClass(cls):
        cls.driver = cls.driver
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
