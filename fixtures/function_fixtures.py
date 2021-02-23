from application import Application
from selenium.webdriver.chrome.options import Options
from settings import local_settings
from settings import global_settings
import pytest


# @pytest.fixture(scope='session')
# def global_chrome_options(request):
#     chrome_options = Options()
#     chrome_options.add_argument('no-sandbox')
#     chrome_options.page_load_strategy = 'normal'
#     chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
#     headless_mode = request.config.getoption('--headless')
#     if headless_mode:
#         chrome_options.add_argument('headless')
#         chrome_options.add_argument('window-size=1920x1080')
#     return chrome_options

@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.binary_location = local_settings.CHROMEDRIVER_PATH
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
