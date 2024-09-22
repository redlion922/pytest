# 搜尋頁
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class SearchPage(BasePage):

    # Locators
    product_img = (By.XPATH, "//body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/a[1]/div[1]/div[1]/div[1]/figure[1]")

    # Actions
    # 點擊第一個商品
    def product(self):
        self.wait_click(self.product_img, 5)
        return self