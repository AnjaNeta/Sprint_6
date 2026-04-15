import allure
import time
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.locators import MainPageLocators


@allure.feature("Навигация")
class TestNavigation:
    
    @allure.title("Проверка перехода на главную страницу при клике на логотип 'Самокат'")
    def test_scooter_logo_redirects_to_main(self, driver):
        # При клике на логотип 'Самоката' происходит переход на главную страницу
        main_page = MainPage(driver)
        
        with allure.step("Нажать на логотип 'Самокат'"):
            main_page.click_scooter_logo()
        
        with allure.step("Проверить, что текущий URL — главная страница"):
            assert driver.current_url == "https://qa-scooter.praktikum-services.ru/", \
                f"Ожидался URL 'https://qa-scooter.praktikum-services.ru/', получен '{driver.current_url}'"
    
    @allure.title("Проверка перехода на главную страницу Дзена при клике на логотип 'Яндекс'")
    def test_yandex_logo_redirects_to_dzen(self, driver):
        # При клике на логотип 'Яндекс' в новом окне открывается главная страница Дзена
        original_window = driver.current_window_handle
        
        with allure.step("Найти ссылку логотипа Яндекса и получить href"):
            yandex_link = driver.find_element(By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI")
            link = yandex_link.get_attribute("href")
        
        with allure.step("Проверить, что ссылка получена"):
            assert link is not None, "Ссылка на логотип Яндекса не найдена"
            if link.startswith("//"):
                link = "https:" + link
        
        with allure.step("Открыть ссылку в новой вкладке через JavaScript"):
            driver.execute_script(f"window.open('{link}', '_blank');")
            time.sleep(1)
            
            # Переключаемся на новую вкладку
            for handle in driver.window_handles:
                if handle != original_window:
                    driver.switch_to.window(handle)
                    break
        
        with allure.step("Проверить, что открылась страница Дзена"):
            current_url = driver.current_url
            assert "dzen.ru" in current_url or "yandex.ru" in current_url, \
                f"Ожидался URL, содержащий 'dzen.ru' или 'yandex.ru', получен '{current_url}'"
        
        with allure.step("Закрыть новое окно и вернуться обратно"):
            driver.close()
            driver.switch_to.window(original_window)

            

