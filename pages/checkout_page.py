# 結帳頁

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class CheckoutPage(BasePage):

    # Locators
    email_input = (By.XPATH, "//input[@placeholder='輸入Email']")

    # Actions
    #輸入email
    def email(self):
        self.wait_input(self.email_input, 5, "redlion922@gmail.com")
        return self