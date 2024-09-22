# 商品頁

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class ProductPage(BasePage):
    # Locators
    # 立即結帳
    checkout_button = (By.XPATH, "//button[@class='core-btn immediately-buy-btn cms-primaryBtnBgColor cms-primaryBtnTextColor cms-primaryBtnBorderColor custom-btn']")
    # 加入購物車
    add_to_cart_button = (By.XPATH, "//button[@class='sale-page-btn core-btn add-to-cart-btn custom-btn cms-secondBtnBgColor cms-secondBtnTextColor cms-secondBtnBorderColor']")

    # Actions
    # 點擊立即結帳
    def checkout(self):
        self.wait_click(self.checkout_button, 5)
        return self

    # 點擊加入購物車
    def add_to_cart(self):
        self.wait_click(self.add_to_cart_button, 5)
        return self



    
