from selenium.webdriver.common.by import By


class Locator:

    def __init__(self, by, locator):
        self.by = by
        self.locator = locator

    def __call__(self, *args, **kwargs):
        return Locator(self.by, self.locator.format(*args))

    def __get__(self):
        return self.by, self.locator


class BaseLocators:
    DIV_CONTAINS_TEXT = Locator(By.XPATH, "//div[contains(text(),'{}')]")


class MainPageLocators:
    ADDRESS_INPUT = Locator(By.CSS_SELECTOR, '.location-panel-search-input')
