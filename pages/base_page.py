from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    # Базовый класс для всех страниц
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def click_element(self, locator):
        # Кликнуть на элемент
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def send_keys(self, locator, text):
        # Ввести текст в поле
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        # Получить текст элемента
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
    
    def is_element_visible(self, locator):
        # Проверить, видим ли элемент
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except:
            return False
    
    def scroll_to_element(self, locator):
        # Прокрутить страницу до элемента
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_current_url(self):
        # Возвращает текущий URL страницы
        return self.driver.current_url
    
    def find_element(self, locator):
        # Находит элемент на странице
        return self.driver.find_element(*locator)
    
    def get_current_window_handle(self):
    # Возвращает идентификатор текущего окна
        return self.driver.current_window_handle


        