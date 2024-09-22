# 登入頁

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class LoginPage(BasePage):

    # Locators
    #輸入手機號碼框
    phone_number_input = (By.XPATH, "//input[@placeholder='輸入手機號碼']")
    register_login_button = (By.XPATH, "//button[contains(text(),'登入/註冊')]")
    password_input = (By.XPATH, "//input[@placeholder='請輸入密碼']")
    login_button = (By.XPATH, "//button[contains(text(),'登入')]")

    # Actions
    # 點擊登入並結帳按鈕
    def login(self):
        self.wait_input(self.phone_number_input, 5, "測試手機號碼")
        self.wait_element_visible(self.register_login_button)
        self.force_click(self.register_login_button)
        self.wait_input(self.password_input, 5, "測試密碼")
        self.wait_element_visible(self.login_button)
        self.force_click(self.login_button)
        return self