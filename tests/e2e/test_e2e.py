import pytest
import allure
from selenium import webdriver
from pages.home_page import HomePage
from pages.ad_page import AdPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
from pages.search_page import SearchPage
from pages.category_page import CategoryPage

@pytest.fixture
def driver():
    # 設置 WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # 測試結束後關閉 WebDriver
    driver.quit()
@allure.story('透過廣告到結帳')
def test_banner_ad_to_checkout_flow(driver):
    # 創建實例
    home_page = HomePage(driver)
    ad_page = AdPage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)
    login_page = LoginPage(driver)
    checkout_page = CheckoutPage(driver)
    # 打開首頁
    driver.get("https://shop.cosmed.com.tw/")
    #關閉蓋板廣告
    home_page.pop_ad_close()
    #點擊cookie同意
    home_page.cookie()
    #點擊首頁廣告
    home_page.banner()
    #點擊第一個商品
    ad_page.product()
    #點擊立即結帳
    product_page.checkout()
    #點擊登入並且結帳按鈕
    cart_page.login_checkout()
    #登入
    login_page.login()
    #點擊結帳
    cart_page.checkout()
    #輸入email
    checkout_page.email()

@allure.story('透過搜尋到結帳')
def test_search_to_checkout_flow(driver):
    # 創建實例
    home_page = HomePage(driver)
    search_page = SearchPage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)
    login_page = LoginPage(driver)
    checkout_page = CheckoutPage(driver)
    # 打開首頁
    driver.get("https://shop.cosmed.com.tw/")
    #關閉蓋板廣告
    home_page.pop_ad_close()
    #點擊cookie同意
    home_page.cookie()
    #點擊搜尋
    home_page.search()
    #點擊第一個商品
    search_page.product()
    #點擊立即結帳
    product_page.checkout()
    #點擊登入並且結帳按鈕
    cart_page.login_checkout()
    #登入
    login_page.login()
    #點擊結帳
    cart_page.checkout()
    #輸入email
    checkout_page.email()

@allure.story('透過分類到結帳')
def test_category_to_checkout_flow(driver):
    # 創建實例
    home_page = HomePage(driver)
    category_page = CategoryPage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)
    login_page = LoginPage(driver)
    checkout_page = CheckoutPage(driver)
    # 打開首頁
    driver.get("https://shop.cosmed.com.tw/")
    #關閉蓋板廣告
    home_page.pop_ad_close()
    #點擊cookie同意
    home_page.cookie()
    #點擊分類
    home_page.category()
    #點擊第一個商品
    category_page.product()
    #點擊立即結帳
    product_page.checkout()
    #點擊登入並且結帳按鈕
    cart_page.login_checkout()
    #登入
    login_page.login()
    #點擊結帳
    cart_page.checkout()
    #輸入email
    checkout_page.email()
