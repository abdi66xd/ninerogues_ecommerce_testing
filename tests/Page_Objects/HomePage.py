from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.success_message_xpath = '//*[@id="root"]/div/div[2]/div/div[2]/p'
        self.profile_icon_css = '.inline-block.h-10.w-10.rounded-full.overflow-hidden.bg-gray-100'
        self.dashboard_option_css = 'Dashboard'
        self.search_name = "search"
        self.shop_text_css = "a[class='mt-2 text-base font-medium text-gray-500 hover:text-gray-900']"
        self.shop_collection_button_xpath = '//*[@id="root"]/div/div[3]/div[1]/div/div/div[2]/div/a'
        self.search_icon_xpath = '//*[@id="root"]/div/div[1]/div[2]/div/div[3]/nav/form/div/div/button'
        self.shop_text_xpath = "//a[normalize-space()='Shop']"

    def get_success_message(self):
        return self.driver.find_element(By.XPATH, self.success_message_xpath).text

    def click_profile_icon(self):
        self.driver.find_element(By.CSS_SELECTOR, self.profile_icon_css).click()

    def click_dashboard_option(self):
        self.driver.find_element(By.LINK_TEXT, self.dashboard_option_css).click()

    def enter_data_search(self, data):
        self.driver.find_element(By.NAME, self.search_name).send_keys(data)

    def click_search_icon(self):
        self.driver.find_element(By.XPATH, self.search_icon_xpath).click()

    def click_shop_collection(self):
        self.driver.find_element(By.XPATH, self.shop_collection_button_xpath).click()

    def click_shop_text(self):
        self.driver.find_element(By.XPATH, self.shop_text_xpath).click()
