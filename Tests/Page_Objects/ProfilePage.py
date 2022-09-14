import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.address_line1_name = "address_line_1"
        self.address_line2_name = "address_line_2"
        self.city_name = "city"
        self.state_province_name = "state_province_region"
        self.postal_code_zipcode_name = 'zipcode'
        self.phone_name = 'phone'
        self.country_region_name = 'country_region'
        self.save_button_css = "button[type='submit']"

    def enter_address1(self, address1):
        # self.driver.find_element(By.NAME, self.address_line1_name).clear()
        self.driver.find_element(By.NAME, self.address_line1_name).click()
        self.driver.find_element(By.NAME, self.address_line1_name).send_keys(address1)

    def enter_address2(self, address2):
        # self.driver.find_element(By.NAME, self.address_line2_name).clear()
        self.driver.find_element(By.NAME, self.address_line2_name).send_keys(address2)

    def enter_city(self, city):
        # self.driver.find_element(By.NAME, self.city_name).clear()
        self.driver.find_element(By.NAME, self.city_name).send_keys(city)

    def enter_state_province(self, province):
        # self.driver.find_element(By.NAME, self.state_province_name).clear()
        self.driver.find_element(By.NAME, self.state_province_name).send_keys(province)

    def enter_postal_code(self, postalcode):
        # self.driver.find_element(By.NAME, self.postal_code_zipcode_name).clear()
        self.driver.find_element(By.NAME, self.postal_code_zipcode_name).send_keys(postalcode)

    def enter_phone(self, phone):
        # self.driver.find_element(By.NAME, self.phone_name).clear()
        self.driver.find_element(By.NAME, self.phone_name).send_keys(phone)

    def enter_country(self, country):
        selection = Select(self.driver.find_element(By.NAME, 'country_region'))
        selection.select_by_value(country)

    def click_save_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.save_button_css).click()

    def get_address_line1_name_placeholder(self):
        return self.driver.find_element(By.NAME, self.address_line1_name).get_attribute("placeholder")

    def get_address_line2_name_placeholder(self):
        return self.driver.find_element(By.NAME, self.address_line2_name).get_attribute("placeholder")

    def get_city_name_placeholder(self):
        return self.driver.find_element(By.NAME, self.address_line1_name).get_attribute("placeholder")

    def get_state_province_name_placeholder(self):
        return self.driver.find_element(By.NAME, self.address_line1_name).get_attribute("placeholder")

    def get_postal_code_zipcode_name_placeholder(self):
        return self.driver.find_element(By.NAME, self.address_line1_name).get_attribute("placeholder")

    def get_phone_name_placeholder_placeholder(self):
        return self.driver.find_element(By.NAME, self.address_line1_name).get_attribute("placeholder")

    def get_country_region_name_placeholder(self):
        return self.driver.find_element(By.NAME, self.address_line1_name).get_attribute("placeholder")


