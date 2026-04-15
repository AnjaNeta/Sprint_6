import allure
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from pages.locators import OrderPageLocators


class OrderPage(BasePage):
    # Класс для страницы заказа
    
    @allure.step("Заполнить форму 'Для кого самокат'")
    def fill_personal_info(self, name, surname, address, phone):
        self.send_keys(OrderPageLocators.NAME_INPUT, name)
        self.send_keys(OrderPageLocators.SURNAME_INPUT, surname)
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, address)
        
        self.click_element(OrderPageLocators.METRO_STATION)
        self.click_element(OrderPageLocators.METRO_OPTION)
        
        self.send_keys(OrderPageLocators.PHONE_INPUT, phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)
    
    @allure.step("Заполнить форму 'Про аренду'")
    def fill_rental_info(self, date, comment):
    # Вводим дату
        self.send_keys(OrderPageLocators.DATE_INPUT, date)
    
    # Закрываем календарь (нажимаем Enter или Esc)
        self.driver.find_element(*OrderPageLocators.DATE_INPUT).send_keys(Keys.ENTER)
    
    # Небольшая пауза, чтобы календарь закрылся
        import time
        time.sleep(0.5)
    
    # Выбираем срок аренды
        self.click_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_element(OrderPageLocators.RENTAL_OPTION)
    
    # Выбираем цвет самоката
        self.click_element(OrderPageLocators.COLOR_BLACK)
    
    # Вводим комментарий
        self.send_keys(OrderPageLocators.COMMENT_INPUT, comment)
    
    # Нажимаем кнопку заказа
        self.click_element(OrderPageLocators.ORDER_BUTTON)
    
    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)
    
    @allure.step("Проверить, что заказ успешно создан")
    def is_order_successful(self):
        return self.is_element_visible(OrderPageLocators.SUCCESS_MESSAGE)
    

    
