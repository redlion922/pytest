# 搜尋頁
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class CategoryPage(BasePage):

    # Locators
    product_img = (By.XPATH, "//*[@id='root']/div[1]/div[2]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/a[1]/div[1]/div[1]/div[1]/figure[1]/img[1]")

    # Actions
    # 點擊第一個商品
    def product(self):
        self.wait_click(self.product_img, 5)
        return self