import allure
from pages.main_page import MainPage


@allure.feature("Навигация")
class TestNavigation:
    
    @allure.title("Проверка перехода на главную страницу при клике на логотип 'Самокат'")
    def test_scooter_logo_redirects_to_main(self, driver):
        # При клике на логотип 'Самоката' происходит переход на главную страницу
        main_page = MainPage(driver)
        
        with allure.step("Нажать на логотип 'Самокат'"):
            main_page.click_scooter_logo()
        
        with allure.step("Проверить, что текущий URL — главная страница"):
            assert main_page.is_on_main_page(), \
                f"Ожидался URL 'https://qa-scooter.praktikum-services.ru/', получен '{main_page.get_current_url()}'"
    
    @allure.title("Проверка перехода на главную страницу Дзена при клике на логотип 'Яндекс'")
    def test_yandex_logo_redirects_to_dzen(self, driver):
        # При клике на логотип 'Яндекс' в новом окне открывается главная страница Дзена
        main_page = MainPage(driver)
        original_window = main_page.get_current_window_handle()
        
        with allure.step("Получить ссылку из логотипа Яндекса"):
            link = main_page.get_yandex_logo_link()
        
        with allure.step("Открыть ссылку в новой вкладке"):
            main_page.open_link_in_new_tab(link)
            main_page.switch_to_new_window(original_window)
        
        with allure.step("Проверить, что открылась страница Дзена"):
            assert main_page.is_on_dzen_page() or main_page.is_on_yandex_page(), \
                f"Ожидался URL, содержащий 'dzen.ru' или 'yandex.ru', получен '{main_page.get_current_url()}'"
        
        with allure.step("Закрыть новое окно и вернуться обратно"):
            main_page.close_current_window_and_switch_back(original_window)

            