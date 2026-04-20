# Автотесты для сервиса «Яндекс.Самокат»

## Описание
Проект содержит UI-автотесты для учебного сервиса «Яндекс.Самокат».

## Структура проекта
qa-scooter-tests/
├── .gitignore
├── requirements.txt
├── conftest.py
├── allure-results/ 
├── pages/
│   ├── base_page.py
│   ├── main_page.py
│   ├── order_page.py
│   └── locators.py
├── tests/
│   ├── test_faq.py
│   ├── test_order.py
│   └── test_navigation.py
└── README.md


## Технологии
- Python 3.11
- Selenium
- Pytest
- Allure
- Page Object Model

## Установка и запуск

Для Chrome (по умолчанию): pytest tests/ -v
Для Firefox: pytest tests/ --browser firefox -v

1. Клонировать репозиторий
2. Установить зависимости:
```bash
pip3 freeze > requirements.txt

# 1. Перейти в папку проекта
cd /путь/проект

# 3. Установить зависимости
pip3 freeze > requirements.txt

# 4. Запустить тесты с сохранением Allure-результатов
pytest tests/ --alluredir=allure-results -v
pytest tests/ --browser firefox --alluredir=allure-results -v

# 5. Сгенерировать и открыть Allure-отчёт
allure serve allure-results

# Запуск по отдельности для проверок успешности прохождения
pytest tests/test_faq.py -v --browser firefox
pytest tests/test_order.py -v --browser firefox
pytest tests/test_navigation.py -v --browser firefox

