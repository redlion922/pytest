# 商品頁

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class CartPage(BasePage):

    # Locators
    login_checkout_button = (By.XPATH, "//button[contains(text(),'登入並結帳')]")
    login_button =(By.XPATH, "//span[contains(text(),'立即登入')]")
    checkout_button = (By.XPATH, "//button[contains(text(),'前往結帳')]")

    # Actions
    # 點擊登入並結帳按鈕
    def login_checkout(self):
        self.wait_element_visible(self.login_checkout_button)
        self.force_click(self.login_checkout_button)
        self.wait_click(self.login_button, 5)
        return self
    #點擊結帳按鈕
    def checkout(self):
        self.wait_element_visible(self.checkout_button)
        self.force_click(self.checkout_button)
        return self
