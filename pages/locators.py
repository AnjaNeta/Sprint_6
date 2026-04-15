from selenium.webdriver.common.by import By


class MainPageLocators:
    # Локаторы главной страницы
    # Кнопки заказа
    ORDER_BUTTON_HEADER = (By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']")
    ORDER_BUTTON_MIDDLE = (By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']")
    
    # Логотипы
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    # Логотип Яндекса (ссылка)
    YANDEX_LOGO_LINK = (By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI")
    # Локатор для картинки
    YANDEX_LOGO_IMAGE = (By.XPATH, "//img[@alt='Yandex']")
    
    # Блок "Вопросы о важном"
    FAQ_BLOCK = (By.CLASS_NAME, "Home_FAQ__3uVm4")
    
    # Вопросы (индексы от 0 до 7)
    FAQ_QUESTIONS = {
        0: (By.ID, "accordion__heading-0"),
        1: (By.ID, "accordion__heading-1"),
        2: (By.ID, "accordion__heading-2"),
        3: (By.ID, "accordion__heading-3"),
        4: (By.ID, "accordion__heading-4"),
        5: (By.ID, "accordion__heading-5"),
        6: (By.ID, "accordion__heading-6"),
        7: (By.ID, "accordion__heading-7"),
    }
    
    # Ответы на вопросы
    FAQ_ANSWERS = {
        0: (By.ID, "accordion__panel-0"),
        1: (By.ID, "accordion__panel-1"),
        2: (By.ID, "accordion__panel-2"),
        3: (By.ID, "accordion__panel-3"),
        4: (By.ID, "accordion__panel-4"),
        5: (By.ID, "accordion__panel-5"),
        6: (By.ID, "accordion__panel-6"),
        7: (By.ID, "accordion__panel-7"),
    }


class OrderPageLocators:
    # Локаторы страницы заказа
    # Форма "Для кого самокат"
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION = (By.XPATH, "//div[@class='Order_Text__2broi' and contains(text(), 'Сокольники')]")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    # Форма "Про аренду"
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-control")
    RENTAL_OPTION = (By.XPATH, "//div[@class='Dropdown-option' and text()='двое суток']")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    
    # Сообщение об успешном заказе
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ') and text()='Заказ оформлен']")

    