from application import Application
from settings import global_settings
import pytest


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument('no-sandbox')
    chrome_options.add_argument("--disable-dev-shm-usage")
    return chrome_options


@pytest.fixture(scope='function')
def selenium_function(chrome_options, selenium):
    selenium.implicitly_wait(global_settings.IMPLICITLY_WAIT)
    selenium.maximize_window()
    return selenium


@pytest.fixture
def app_function(selenium_function):
    browser = Application(selenium=selenium_function)
    yield browser
    return browser
