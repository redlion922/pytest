# tests/conftest.py

import pytest
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import allure

# 添加專案根目錄到 sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture(scope='session')
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # 無頭模式
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    # 使用 Service 類來指定 ChromeDriver 的路徑
    service = Service(ChromeDriverManager().install())
    
    # 初始化 WebDriver，避免參數衝突
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
