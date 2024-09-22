# Pytest_91APP

## 專案簡介

Pytest_91APP 是一個基於 [Pytest](https://docs.pytest.org/) 的自動化測試框架，採用 Page Object Model（頁面物件模型）設計模式，旨在對 91APP 應用進行全面的 API 和端到端（E2E）測試。專案整合了 Allure 報告，提供詳細的測試執行報告，幫助開發和測試團隊快速定位問題。

## 目錄結構

```
Pytest_91APP
├── pages
│   ├── __init__.py
│   ├── ad_page.py
│   ├── base_page.py
│   ├── cart_page.py
│   ├── category_page.py
│   ├── checkout_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── product_page.py
│   └── search_page.py
├── reports
│   ├── allure
│   └── report
├── tests
│   ├── api
│   ├── e2e
│   ├── conftest.py
│   └── pytest.ini
├── .gitignore
├── README.md
└── requirements.txt
```

## 先決條件

- Python 3.7+
- pip
- Git
- allure

## 安裝

1. **克隆倉庫**

   ```bash
   git clone https://github.com/yourusername/Pytest_91APP.git
   cd Pytest_91APP
   ```

2. **安裝相依**

   ```bash
   pip install -r requirements.txt
   ```

## 配置

根據專案需求，編輯 `tests/pytest.ini` 以配置 Pytest 選項。例如，可以配置測試路徑、報告生成選項等。

## 使用

### 執行所有測試

```bash
pytest
```

### 執行特定測試目錄

- **API 測試**

  ```bash
  pytest tests/api
  ```

- **端到端（E2E）測試**

  ```bash
  pytest tests/e2e
  ```

### 生成 Allure 報告

1. **執行測試並生成 Allure 原始報告**

   ```bash
   pytest --alluredir=reports/allure
   ```

2. **生成並查看 Allure 報告**

   ```bash
   allure generate reports/allure -o reports/report --clean
   ```

   > **注意**: 需要先安裝 [Allure](https://docs.qameta.io/allure/#_installing_a_commandline) 命令列工具。

### 查看測試報告

生成的測試報告位於 `reports/report` 目錄，可以根據需要查看詳細的測試執行結果。

## 專案結構說明

- **pages/**: 頁面物件模型（POM）資料夾，包含各個頁面的操作封裝。
  - `base_page.py`: 基礎頁面類，提供通用方法。
  - 其他頁面檔案如 `login_page.py`, `cart_page.py` 等，封裝了對應頁面的操作。
  
- **tests/**: 測試案例資料夾，分為 API 測試和 E2E 測試。
  - `api/`: 存放 API 測試案例。
  - `e2e/`: 存放端到端測試案例。
  - `conftest.py`: Pytest 配置檔案，包含夾具（fixtures）等共享配置。
  - `pytest.ini`: Pytest 配置檔案，配置測試選項。
  
- **reports/**: 測試報告資料夾。
  - `allure/`: Allure 原始報告檔案。
  - `report/`: 生成的測試報告。
  
- **requirements.txt**: 專案相依套件列表。
