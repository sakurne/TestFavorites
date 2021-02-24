from pages.base_page import BasePage
from pages.search_restaurant_page import SearchRestaurantPage
from locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, app, base_url):
        super(MainPage, self).__init__(app, base_url)

    # base_url = settings.MAIN_PAGE_ENG

    def search_address(self, address):
        self.fill_input_field(*MainPageLocators.ADDRESS_INPUT, address)
        self.click_element(*MainPageLocators.SEARCH_ADDRESS)
        self.app.current_page = SearchRestaurantPage(self.app)
