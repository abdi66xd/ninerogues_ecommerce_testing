from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.shopping_cart_message_xpath = "h1[class='text-3xl font-extrabold tracking-tight text-gray-900 " \
                                           "sm:text-4xl'] "
        self.x_icon_xpath = "//ul[@class='border-t border-b border-gray-200 divide-y divide-gray-200']//div[" \
                            "@class='absolute top-0 right-0']//button[@class='-m-2 p-2 inline-flex text-gray-400 " \
                            "hover:text-gray-500']//*[name()='svg'] "

    def get_cart_items_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.shopping_cart_message_xpath).text

    def click_x_icon(self):
        self.driver.find_element(By.XPATH, self.x_icon_xpath).click()
