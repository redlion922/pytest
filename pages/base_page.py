from ast import literal_eval
from time import sleep
import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


class BasePage():

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def open_url(self, url):
        # 打開指定的 URL
        self.driver.get(url)

    def format_locator(locator, values):
        # 格式化定位符
        return literal_eval(str(locator) % values)

    def get_element(self, by_locator):
        # 獲取單個元素
        return self.driver.find_element(*by_locator)

    def get_elements(self, by_locator):
        # 獲取多個元素
        return self.driver.find_elements(*by_locator)

    def has_element(self, by_locator) -> bool:
        # 檢查元素是否存在
        self.driver.implicitly_wait(3)
        elements = self.driver.find_elements(*by_locator)
        self.driver.implicitly_wait(20)
        return len(elements) > 0

    def get_current_url(self):
        # 獲取當前頁面的 URL
        return self.driver.current_url

    def sleep(self, seconds):
        # 暫停執行（休眠）
        sleep(seconds)
        return self

    def change_focused(self):
        # 切換焦點（TAB 鍵）
        ActionChains(self.driver).send_keys(Keys.TAB).perform()

    def scroll_page_down(self):
        # 向下滾動頁面
        ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()

    def scroll_page_up(self):
        # 向上滾動頁面
        ActionChains(self.driver).send_keys(Keys.PAGE_UP).perform()

    def scroll_to_top(self):
        # 滾動至頁面頂部
        self.driver.execute_script("window.scrollTo(0, 0);")

    def scroll_to_bottom(self):
        # 滾動至頁面底部
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_element_top(self, by_locator):
        # 滾動至元素的頂部
        element = self.get_element(by_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_to_element(self, by_locator):
        # 滾動至元素（頁面中間）
        element = self.get_element(by_locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def click(self, by_locator):
        # 點擊元素
        self.driver.find_element(*by_locator).click()

    def input(self, by_locator, text):
        # 在元素中輸入文字
        element = self.driver.find_element(*by_locator)
        element.clear()
        element.send_keys(text)

    def input_by_key(self, by_locator, text):
        # 透過按鍵操作輸入文字（選中並刪除後輸入）
        element = self.driver.find_element(*by_locator)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(text)

    def get_title(self):
        # 獲取頁面標題
        print(self.driver.title)

    def get_text(self, by_locator):
        # 獲取元素的文字
        return self.driver.find_element(*by_locator).text

    def get_data_from_attribute(self, by_locator, attribute):
        # 獲取元素屬性的數據
        return self.driver.find_element(*by_locator).get_attribute(attribute)

    def get_input_value(self, by_locator):
        # 獲取輸入框中的值
        return self.driver.find_element(*by_locator).get_attribute("value")

    def get_select_value(self, by_locator):
        # 獲取下拉選單的選擇值
        select = Select(self.driver.find_element(*by_locator))
        return select.first_selected_option.text

    def set_select_value(self, by_locator, val):
        # 設置下拉選單的選擇值
        select = Select(self.driver.find_element(*by_locator))
        select.select_by_visible_text(val)

    def wait_click(self, by_locator, wait_seconds):
        # 等待元素可點擊，然後點擊
        WebDriverWait(self.driver, wait_seconds).until(
            EC.element_to_be_clickable(by_locator)).click()

    def wait_input(self, by_locator, wait_seconds, text):
        # 等待元素可見，然後輸入文字
        return WebDriverWait(
            self.driver, wait_seconds).until(
            EC.visibility_of_element_located(by_locator)).send_keys(text)

    def wait_get_title(self, title, wait_seconds) -> str:
        # 等待並獲取頁面標題
        WebDriverWait(self.driver, wait_seconds).until(EC.title_is(title))
        return self.driver.title

    def accept_alert(self):
        # 接受彈出警示框
        WebDriverWait(self.driver, 3).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

    def get_alert_text(self):
        # 獲取警示框中的文字
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        return alert.text

    def wait_text_to_be(self, by_locator, text):
        # 等待元素中的文字符合指定條件
        WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element(by_locator, text))

    def wait_element_invisible(self, by_locator):
        # 等待元素不可見
        WebDriverWait(self.driver, 30).until(
            EC.invisibility_of_element_located(by_locator))

    def wait_element_visible(self, by_locator):
        # 等待元素可見
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(by_locator))

    def move_to_element(self, by_locator):
        # 移動滑鼠到指定元素
        target_element = self.get_element(by_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(target_element).perform()

    def move_mouse_offset(self, x_offset, y_offset):
        # 根據偏移量移動滑鼠
        actions = ActionChains(self.driver)
        actions.move_by_offset(x_offset, y_offset).perform()

    def switch_to_window(self, window_index):
        # 切換至指定的窗口
        self.driver.switch_to.window(self.driver.window_handles[window_index])

    def close_current_window(self):
        # 關閉當前窗口
        self.driver.close()

    def get_entire_window(self):
        # 獲取當前所有窗口的數量
        return len(self.driver.window_handles)

    def switch_to_frame(self, frame_id):
        # 切換到指定的框架
        self.driver.switch_to.frame(frame_id)
        return self

    def switch_to_default(self):
        # 切換回預設的框架
        self.driver.switch_to.default_content()
        return self

    def wait_url_changed(self):
        # 等待 URL 變更
        old_url = self.driver.current_url
        WebDriverWait(self.driver, 10).until(lambda driver: old_url != driver.current_url)

    def wait_specific_url_changed(self, url):
        # 等待 URL 變更為特定內容
        WebDriverWait(self.driver, 10).until(EC.url_contains(url))
        return self

    def get_screenshot_as_png(self, title):
        # 截圖並保存為 PNG 格式
        if hasattr(self.driver, "get_screenshot_as_png"):
            allure.attach(self.driver.get_screenshot_as_png(), title, allure.attachment_type.PNG)

    def navigate_back(self):
        # 返回上一頁
        self.driver.execute_script("window.history.go(-1)")

    def element_is_displayed(self, by_locator):
        # 檢查元素是否顯示
        elem = self.get_element(by_locator)
        return elem.is_displayed()

    def element_in_viewport(self, by_locator):
        # 檢查元素是否在視口範圍內
        elem = self.get_element(by_locator)
        elem_left_bound = elem.location.get('x')
        elem_top_bound = elem.location.get('y')
        elem_width = elem.size.get('width')
        elem_height = elem.size.get('height')
        elem_right_bound = elem_left_bound + elem_width
        elem_lower_bound = elem_top_bound + elem.height

        win_upper_bound = self.driver.execute_script('return window.pageYOffset')
        win_left_bound = self.driver.execute_script('return window.pageXOffset')
        win_width = self.driver.execute_script('return document.documentElement.clientWidth')
        win_height = self.driver.execute_script('return document.documentElement.clientHeight')
        win_right_bound = win_left_bound + win_width
        win_lower_bound = win_upper_bound + win_height

        return all((win_left_bound <= elem_left_bound,
                    win_right_bound >= elem_right_bound,
                    win_upper_bound <= elem_top_bound,
                    win_lower_bound >= elem_lower_bound))
    
    def force_click(self, by_locator):
        #強制點擊
        element = self.driver.find_element(*by_locator)
        self.driver.execute_script("arguments[0].click();", element)