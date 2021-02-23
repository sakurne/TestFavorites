from pages.base_page import BasePage
from locators import MainPageLocators
import settings


class MainPage(BasePage):
    def __init__(self, app, base_url):
        super(MainPage, self).__init__(app, base_url)

    # base_url = settings.MAIN_PAGE_ENG

    def search_address(self, address):
        self.fill_input_field(*MainPageLocators.ADDRESS_INPUT, address)
