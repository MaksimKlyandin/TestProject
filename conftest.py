import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from faker import Faker

default_lang = "ru"
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="None",
                 help="Choose language: ru or es")

@pytest.fixture(scope="function")
def browser(request):
    browser_lang = request.config.getoption("language")    
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_lang})   
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(options=options)   
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope="function")
def faker():
    return Faker()