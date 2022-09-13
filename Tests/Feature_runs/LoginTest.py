from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from Tests.Page_Objects.LoginPage import LoginPage
from Tests.Page_Objects.HomePage import HomePage
from selenium.webdriver.chrome.service import Service

# Data set to test
valid_username = "abdiasalpire12+20@gmail.com"
valid_password = "7928003cba"
invalid_username = "abdiasalpire12+1''@gmail.com"
invalid_password = "never_used_password"


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('D:/tutos/ninerogues_ecommerce/Tests/Drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_valid_login(self):
        driver = self.driver
        self.driver.get("http://localhost:3000/login")
        time.sleep(5)
        login = LoginPage(driver)
        login.enter_username(valid_username)
        login.enter_password(valid_password)
        login.click_login_button()
        home = HomePage(driver)
        success_message = home.get_success_message()
        time.sleep(3)
        self.assertEqual('Inicio de sesión con éxito', success_message)

    def test_invalid_login(self):
        driver = self.driver
        self.driver.get("http://localhost:3000/login")
        time.sleep(5)
        login = LoginPage(driver)
        login.enter_username(invalid_username)
        login.enter_password(invalid_password)
        login.click_login_button()
        home = HomePage(driver)
        fail_message = home.get_success_message()
        time.sleep(3)
        self.assertEqual('Error al iniciar sesion. Intenta mas tarde', fail_message)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
