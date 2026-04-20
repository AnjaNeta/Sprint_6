import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome or firefox")


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    
    if browser_name == "chrome":
        options = Options()
        options.add_argument('--disable-blink-features=AutomationControlled')
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unknown browser: {browser_name}")
    
    driver.get("https://qa-scooter.praktikum-services.ru/")
    driver.maximize_window()
    
    yield driver
    
    driver.quit()

    