import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Tests.Feature_runs.LoginTest import LoginTest
from Tests.Page_Objects.DashboardPage import DashboardPage
from Tests.Page_Objects.HomePage import HomePage
from Tests.Page_Objects.LoginPage import LoginPage
from Tests.Page_Objects.ProfilePage import ProfilePage

# Data set to test
address_line1 = "Avenida Juan Pablo Ii, 155, Urb. San Andrés"
address_line2 = "CA MANUEL MARIA IZAGA 162, CHICLAYO"
city = "Trujillo"
state = "La Libertad"
postalcode = "13001"
phone = "(044)23-3035"
country = "Peru"


class ProfileTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('D:/tutos/ninerogues_ecommerce/Tests/Drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_filling_profile(self):
        driver = self.driver
        self.driver.get("http://localhost:3000/login")
        time.sleep(2)
        login = LoginPage(driver)
        login.enter_username("abdiasalpire12+25@gmail.com")
        login.enter_password("7928003cba")
        login.click_login_button()
        home = HomePage(driver)
        time.sleep(2)
        home.click_profile_icon()
        home.click_dashboard_option()
        time.sleep(2)
        dashboard = DashboardPage(driver)
        driver.back()
        driver.forward()
        time.sleep(2)
        dashboard.click_profile_option()
        profile = ProfilePage(driver)
        profile.enter_address1(address_line1)
        profile.enter_address2(address_line2)
        profile.enter_city(city)
        profile.enter_state_province(state)
        profile.enter_postal_code(postalcode)
        profile.enter_phone(phone)
        profile.enter_country(country)
        profile.click_save_button()
        driver.refresh()
        # Send it back to the home page and repeat the process to check the saved items
        time.sleep(2)
        home.click_profile_icon()
        home.click_dashboard_option()
        time.sleep(2)
        dashboard = DashboardPage(driver)
        driver.back()
        driver.forward()
        time.sleep(2)
        dashboard.click_profile_option()
        self.assertEqual(address_line1, profile.get_address_line1_name_placeholder())

    def fill_form(self):
        driver = self.driver
        self.driver.get("http://localhost:3000/login")
        time.sleep(2)
        login = LoginPage(driver)
        login.enter_username("abdiasalpire12+25@gmail.com")
        login.enter_password("7928003cba")
        login.click_login_button()
        home = HomePage(driver)
        time.sleep(2)
        home.click_profile_icon()
        home.click_dashboard_option()
        time.sleep(2)
        dashboard = DashboardPage(driver)
        driver.back()
        driver.forward()
        time.sleep(2)
        dashboard.click_profile_option()
        profile = ProfilePage(driver)
        profile.enter_address1(address_line1)
        profile.enter_address2(address_line2)
        profile.enter_city(city)
        profile.enter_state_province(state)
        profile.enter_postal_code(postalcode)
        profile.enter_phone(phone)
        profile.enter_country(country)
        profile.click_save_button()
        driver.refresh()

    def validate_form(self):
        driver = self.driver
        self.driver.get("http://localhost:3000/")
        home = HomePage(driver)
        time.sleep(2)
        home.click_profile_icon()
        home.click_dashboard_option()
        time.sleep(2)
        dashboard = DashboardPage(driver)
        driver.back()
        driver.forward()
        time.sleep(2)
        dashboard.click_profile_option()
        profile = ProfilePage(driver)
        self.assertEqual(address_line1, profile.get_address_line1_name_placeholder())
        self.assertEqual(address_line2, profile.get_address_line1_name_placeholder())
        self.assertEqual(address_line1, profile.get_address_line1_name_placeholder())
        self.assertEqual(address_line1, profile.get_address_line1_name_placeholder())
        self.assertEqual(address_line1, profile.get_address_line1_name_placeholder())


    @classmethod
    def tearDownClass(cls):
        cls.driver = cls.driver
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
