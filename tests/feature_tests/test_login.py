from datetime import time

from selenium import webdriver

import shutil
from webdriver_manager.chrome import ChromeDriverManager

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from apps.user.models import UserAccount
from core.settings import BASE_DIR
from tests.feature_tests.constants import FRONTEND_URL
from tests.Page_Objects.LoginPage import LoginPage
from tests.Page_Objects.HomePage import HomePage

# Data set to test
valid_username = "abdiasalpire12+20@gmail.com"
valid_password = "7928003cba"
invalid_username = "abdiasalpire12+1''@gmail.com"
invalid_password = "never_used_password"


class TestLogin(StaticLiveServerTestCase):

    port = 8000

    def setUp(self):
        # cls.driver = webdriver.Chrome('../drivers/chromedriver.exe')
        driver_file = str(BASE_DIR) + '/tests/drivers/chromedriver_105'

        self.new_user = UserAccount.objects.create(
            email=valid_username,
            first_name='Firstname',
            last_name='Lastname',
        )
        self.new_user.set_password(valid_password)
        self.new_user.save()

        if shutil.which('chromedriver'):
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Chrome(ChromeDriverManager().install())

        # cls.driver = webdriver.Chrome(driver_file)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_valid_login(self):
        self.driver.get(FRONTEND_URL + "login")
        login = LoginPage(self.driver)
        time.sleep(2)
        login.enter_username(self.new_user.email)
        login.enter_password(valid_password)
        login.click_login_button()
        home = HomePage(self.driver)
        success_message = home.get_success_message()
        self.assertEqual('Inicio de sesión con éxito', success_message)

    def test_invalid_login(self):
        driver = self.driver
        self.driver.get(FRONTEND_URL + "login")
        login = LoginPage(driver)
        login.enter_username(invalid_username)
        login.enter_password(invalid_password)
        login.click_login_button()
        home = HomePage(driver)
        fail_message = home.get_success_message()
        self.assertEqual(
            'No active account found with the given credentials', fail_message
        )

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
