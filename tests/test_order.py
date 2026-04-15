import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Заказ самоката")
class TestOrder:
    
    @allure.title("Позитивный сценарий заказа самоката через кнопку в шапке")
    @pytest.mark.parametrize("name, surname, address, phone, date, comment", [
        ("Анна", "Добрянская", "ул. Пушкина, 10", "+79991234567", "01.05.2026", "Позвоните за час"),
        ("Петр", "Иванов", "ул. Ленина, 5", "+79997654321", "02.05.2026", "Домофон 123"),
    ])
    def test_order_from_header(self, driver, name, surname, address, phone, date, comment):
        # Тест заказа самоката через кнопку в шапке страницы"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        with allure.step("Нажать кнопку 'Заказать' в шапке"):
            main_page.click_order_button_header()
        
        with allure.step("Заполнить форму 'Для кого самокат'"):
            order_page.fill_personal_info(name, surname, address, phone)
        
        with allure.step("Заполнить форму 'Про аренду'"):
            order_page.fill_rental_info(date, comment)
        
        with allure.step("Подтвердить заказ"):
            order_page.confirm_order()
        
        with allure.step("Проверить, что заказ успешно создан"):
            assert order_page.is_order_successful(), "Сообщение об успешном заказе не появилось"
    
    @allure.title("Позитивный сценарий заказа самоката через кнопку в середине страницы")
    @pytest.mark.parametrize("name, surname, address, phone, date, comment", [
        ("Елена", "Сидорова", "пр. Мира, 15", "+79991112233", "03.05.2026", "Код домофона 456"),
        ("Иван", "Петров", "ул. Садовая, 7", "+79994445566", "04.05.2026", "Вход со двора"),
    ])
    def test_order_from_middle(self, driver, name, surname, address, phone, date, comment):
        # Тест заказа самоката через кнопку в середине страницы
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        with allure.step("Нажать кнопку 'Заказать' в середине страницы"):
            main_page.click_order_button_middle()
        
        with allure.step("Заполнить форму 'Для кого самокат'"):
            order_page.fill_personal_info(name, surname, address, phone)
        
        with allure.step("Заполнить форму 'Про аренду'"):
            order_page.fill_rental_info(date, comment)
        
        with allure.step("Подтвердить заказ"):
            order_page.confirm_order()
        
        with allure.step("Проверить, что заказ успешно создан"):
            assert order_page.is_order_successful(), "Сообщение об успешном заказе не появилось"

            