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

        