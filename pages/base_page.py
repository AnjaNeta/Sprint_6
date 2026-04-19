import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    @allure.step("Кликнуть на элемент")
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    @allure.step("Ввести текст в поле")
    def send_keys(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
    
    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
    
    @allure.step("Проверить видимость элемента")
    def is_element_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except:
            return False
    
    @allure.step("Прокрутить к элементу")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    @allure.step("Найти элемент")
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Получить идентификатор текущего окна")
    def get_current_window_handle(self):
        return self.driver.current_window_handle
    
    @allure.step("Получить атрибут элемента")
    def get_element_attribute(self, locator, attribute_name):
        element = self.find_element(locator)
        return element.get_attribute(attribute_name)
    
    @allure.step("Открыть URL в новой вкладке")
    def open_url_in_new_tab(self, url):
        self.driver.execute_script(f"window.open('{url}', '_blank');")
    
    @allure.step("Форматировать ссылку")
    def format_url(self, url):
        if url and url.startswith("//"):
            return "https:" + url
        return url
    
    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self, original_window_handle):
        # Ждём появления нового окна
        self.wait.until(lambda driver: len(driver.window_handles) > 1)
        
        # Переключаемся на новое окно
        for handle in self.driver.window_handles:
            if handle != original_window_handle:
                self.driver.switch_to.window(handle)
                break
        
        # Ждём, пока URL перестанет быть about:blank
        self.wait.until(lambda driver: driver.current_url != "about:blank")
    
    @allure.step("Закрыть текущее окно и вернуться обратно")
    def close_current_window_and_switch_back(self, original_window_handle):
        self.driver.close()
        self.driver.switch_to.window(original_window_handle)

        