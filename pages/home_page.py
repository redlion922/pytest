# 首頁

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class HomePage(BasePage):

    # Locators
    #slick-track的第一個廣告
    banner_text = (By.XPATH, "//div[contains(text(),'熱銷必買 買1送1')]")
    #搜尋框
    search_box = (By.XPATH, "//input[@id='ns-search-input']")
    #搜尋按鈕
    search_button = (By.XPATH, "//i[@class='ico ico-search']")
    #商品分類
    product_category = (By.XPATH, "//div[@class='sc-icLIcW ekgyNY']")
    #l1
    l1 = (By.XPATH, "//*[@id='root']/div[1]/div[1]/header[1]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[1]/div[1]/ul[1]/li[7]/a[1]")
    # 彈窗廣告關閉
    pop_ad_close_button = (By.XPATH, "//div[@class='sc-iKGpAt kYEqzZ']//*[name()='svg']")
    # cookie同意
    cookie_button = (By.XPATH, "//a[contains(text(),'我知道了')]")

    # Actions
    def pop_ad_close(self):
        self.wait_click(self.pop_ad_close_button, 5)
        return self

    def cookie(self):
        #點擊cookie同意
        self.wait_click(self.cookie_button, 5)
        return self

    def banner(self):
        self.wait_click(self.banner_text, 5)
        return self

    def search(self):
        self.wait_input(self.search_box, 5, "牙刷")
        self.click(self.search_button)
        return self
    
    def category(self):
        self.wait_click(self.product_category, 5)
        self.wait_click(self.l1, 5)
        return self


    
