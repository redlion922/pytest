# 廣告頁

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class AdPage(BasePage):

    # Locators
    #第一個商品
    product_text = (By.XPATH, "//body/div[@id='root']/div[@class='container-component']/div[@class='layout-center']/div[@class='sc-Cvcpl fYHjxo']/div[@class='sc-hZtkDs hhKrRN']/div[@class='sc-lblmNX dUJaFM']/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/a[1]/div[1]/div[2]/div[1]")
    
    # Actions
    #點擊第一個商品
    def product(self):
        self.wait_click(self.product_text, 5)
        return self


    
