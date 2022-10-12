import time
import unittest
from selenium import webdriver

from tests.Page_Objects.RegisterPage import RegisterPage
from tests.feature_tests.constants import FRONTEND_URL
from tests.Page_Objects.HomePage import HomePage

# Data set to test
success_register_message = "Estas registrado!"
first_name = "Luifwefs"
last_name = "Diewefwefgo"
email = "test+6@gmail.com"
password = "7928003cbaA@"
re_password = "7928003cbaA@"


class test_register(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('D:/tutos/ninerogues_ecommerce/tests/drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_register_user(self):
        driver = self.driver
        self.driver.get(FRONTEND_URL + "signup")
        time.sleep(2)
        register = RegisterPage(driver)
        register.enter_first_name(first_name)
        register.enter_last_name(last_name)
        register.enter_email(email)
        register.enter_password(password)
        register.enter_re_password(re_password)
        register.click_register_button()
        time.sleep(2)
        message = register.get_message()
        self.assertEqual(message, success_register_message)

    @classmethod
    def tearDownClass(cls):
        cls.driver = cls.driver
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
