import allure
from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    # Класс для главной страницы
    
    @allure.step("Нажать кнопку 'Заказать' в шапке страницы")
    def click_order_button_header(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_HEADER)
    
    @allure.step("Нажать кнопку 'Заказать' в середине страницы")
    def click_order_button_middle(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_MIDDLE)
        self.click_element(MainPageLocators.ORDER_BUTTON_MIDDLE)
    
    @allure.step("Нажать на вопрос {index}")
    def click_faq_question(self, index):
        self.scroll_to_element(MainPageLocators.FAQ_QUESTIONS[index])
        self.click_element(MainPageLocators.FAQ_QUESTIONS[index])
    
    @allure.step("Получить текст ответа на вопрос {index}")
    def get_faq_answer_text(self, index):
        return self.get_text(MainPageLocators.FAQ_ANSWERS[index])
    
    @allure.step("Нажать на логотип 'Самокат'")
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)
    
    @allure.step("Нажать на логотип 'Яндекс'")
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)
    
    @allure.step("Получить ссылку из логотипа Яндекса")
    def get_yandex_logo_link(self):
        # Возвращает ссылку из логотипа Яндекса"""
        yandex_link = self.find_element(MainPageLocators.YANDEX_LOGO_LINK)
        link = yandex_link.get_attribute("href")
        if link and link.startswith("//"):
            link = "https:" + link
        return link
    
    @allure.step("Открыть ссылку в новой вкладке")
    def open_link_in_new_tab(self, link):
        # Открывает ссылку в новой вкладке через JavaScript"""
        self.driver.execute_script(f"window.open('{link}', '_blank');")
    
    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self, original_window_handle):
        # Переключается на новое окно (не на original_window_handle)"""
        import time
        time.sleep(1)  # Даём время на открытие вкладки
        
        for handle in self.driver.window_handles:
            if handle != original_window_handle:
                self.driver.switch_to.window(handle)
                break
    
    @allure.step("Закрыть текущее окно и вернуться обратно")
    def close_current_window_and_switch_back(self, original_window_handle):
        # Закрывает текущее окно и переключается обратно на исходное"""
        self.driver.close()
        self.driver.switch_to.window(original_window_handle)
    
    @allure.step("Проверить, что текущая страница — главная")
    def is_on_main_page(self):
        # Проверяет, что текущая страница — главная
        return self.get_current_url() == "https://qa-scooter.praktikum-services.ru/"
    
    @allure.step("Проверить, что открылась страница Дзена")
    def is_on_dzen_page(self):
        # Проверяет, что текущая страница — Дзен
        return "dzen.ru" in self.get_current_url()
    
    @allure.step("Проверить, что открылась страница Яндекса")
    def is_on_yandex_page(self):
        # Проверяет, что текущая страница — Яндекс
        return "yandex.ru" in self.get_current_url()
    
    @allure.step("Проверить, что возвращается идентификатор текущего окна")
    def get_current_window_handle(self):
    # Возвращает идентификатор текущего окна
        return super().get_current_window_handle()
    

