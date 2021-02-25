from abc import ABC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import global_settings


class BasePage(ABC):
    def __init__(self, app, base_url=None):
        self.app = app
        if base_url and app.browser.current_url != base_url:
            self.app.open_page(base_url)
        app.current_page = self

    def should_be_element(self, how, what, timeout=global_settings.DEFAULT_TIMEOUT):
        try:
            self.find_when_appeared(how, what, timeout)
        except TimeoutException:
            return False
        return True

    def refresh(self):
        self.app.browser.refresh()

    def click_element(self, how, what, by_cursor=True, scroll=False):
        browser = self.app.browser
        if scroll:
            self.scroll_to_element(how, what)
        if by_cursor:
            element = browser.find_element(how, what)
            ActionChains(browser).move_to_element(element).click(element).perform()
        else:
            browser.find_element(how, what).click()

    def scroll_to_element(self, how, what):
        element = self.find_when_appeared(how, what, timeout=global_settings.DEFAULT_TIMEOUT)
        self.app.browser.execute_script("arguments[0].scrollIntoView(true)", element)

    def scroll(self, x='0', y='0'):
        self.app.browser.execute_script("window.scrollTo(window.scrollX +{}, window.scrollY + {})".format(x, y))

    def find_when_appeared(self, how, what, timeout=global_settings.DEFAULT_TIMEOUT):
        browser = self.app.browser
        element = WebDriverWait(
            browser,
            timeout,
            global_settings.DEFAULT_POLL_FREQUENCY
        ).until(EC.presence_of_element_located((how, what)))
        return element

    def fill_input_field(self, how, what, content):
        browser = self.app.browser
        field = browser.find_element(how, what)
        field.clear()
        field.send_keys(content)

    def get_attribute_from_element(self, how, what, field_name='value'):
        return self.app.browser.find_element(how, what).get_attribute(field_name)

    def count_of_elements(self, how, what, timeout=global_settings.DEFAULT_TIMEOUT, assertion_msg=None):
        try:
            length = len(self.find_elements_when_appeared(how, what, timeout=timeout))
        except TimeoutException:
            raise AssertionError(assertion_msg or 'elements with locator {} are not found'.format(what))
        return length

    def find_elements_when_appeared(self, how, what, timeout=global_settings.DEFAULT_TIMEOUT):
        browser = self.app.browser
        WebDriverWait(browser, timeout).until(EC.presence_of_all_elements_located((how, what)))
        return self.app.browser.find_elements(how, what)
