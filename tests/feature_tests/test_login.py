from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from django.test import TestCase

from apps.user.models import UserAccount
from core.settings import BASE_DIR
from tests.feature_tests.constants import FRONTEND_URL
from tests.Page_Objects.LoginPage import LoginPage
from tests.Page_Objects.HomePage import HomePage
from selenium.webdriver.chrome.service import Service

# Data set to test
valid_username = "abdiasalpire12+20@gmail.com"
valid_password = "7928003cba"
invalid_username = "abdiasalpire12+1''@gmail.com"
invalid_password = "never_used_password"


class TestLogin(TestCase):

    @classmethod
    def setUpClass(cls):
        # cls.driver = webdriver.Chrome('../drivers/chromedriver.exe')
        driver_file = str(BASE_DIR) + '/tests/drivers/chromedriver_105'

        cls.new_user = UserAccount.objects.create(
            email=valid_username,
            first_name='Firstname',
            last_name='Lastname',
        )
        cls.new_user.set_password(valid_password)
        cls.new_user.save()

        cls.driver = webdriver.Chrome(driver_file)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_valid_login(self):
        driver = self.driver
        self.driver.get(FRONTEND_URL + "login")
        time.sleep(5)
        login = LoginPage(driver)

        login.enter_username(self.new_user.email)
        login.enter_password(valid_password)
        login.click_login_button()
        home = HomePage(driver)
        success_message = home.get_success_message()
        time.sleep(1500)
        self.assertEqual('Inicio de sesión con éxito', success_message)

    # def test_invalid_login(self):
    #     driver = self.driver
    #     self.driver.get(FRONTEND_URL + "login")
    #     time.sleep(5)
    #     login = LoginPage(driver)
    #     login.enter_username(invalid_username)
    #     login.enter_password(invalid_password)
    #     login.click_login_button()
    #     home = HomePage(driver)
    #     fail_message = home.get_success_message()
    #     time.sleep(3)
    #     self.assertEqual('Error al iniciar sesion. Intenta mas tarde', fail_message)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
