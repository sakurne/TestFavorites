from selenium.webdriver.common.by import By
import operator


class Locator(tuple):

    __slots__ = ()
    by = property(operator.itemgetter(0))
    locator: str = property(operator.itemgetter(1))

    def __new__(cls, by, locator):
        return tuple.__new__(cls, (by, locator))

    # def insert_substring(self, *substrings):
    #     return self.locator.format(*substrings)

    def __call__(self, *args, **kwargs):
        return Locator(self.by, self.locator.format(*args))

    def __str__(self):
        return self.locator


class BaseLocators:
    OPTIONS_ICON = Locator(By.CSS_SELECTOR, '.menu')
    INDEX_ENDING = '[{}]'


class MainPageLocators:
    ADDRESS_INPUT = Locator(By.CSS_SELECTOR, '.location-panel-search-input')
    SEARCH_ADDRESS = Locator(By.CSS_SELECTOR, '[id="submit_deliveryarea"]')


class SearchRestaurantLocators:
    ALL_RESTAURANTS = Locator(By.XPATH, '//div[@class = "restaurant js-restaurant"]')
    RESTAURANT_BY_INDEX = Locator(By.XPATH, '(//div[@class = "restaurant js-restaurant"])[{}]')
    RESTAURANTS_OPENED = Locator(
        By.XPATH,
        '//div[@class="js-restaurant-list-open"]//div[@class = "restaurant js-restaurant"]'
    )

    RESTAURANTS_PREORDER = Locator(
        By.XPATH,
        '//div[contains(@class, "js-restaurant-list-preorder")]//div[@class = "restaurant js-restaurant"]'
    )

    RESTURANTS_CLOSED = Locator(
        By.XPATH,
        '//div[contains(@class, "js-restaurant-list-closed")]//div[@class = "restaurant js-restaurant"]'
    )
    RESTAURANT_NAME_ENDING = '//a[contains(@class,"restaurantname")]'
    RESTAURANT_DELIVERY_TIME_ENDING = '//div[contains(@class, "avgdeliverytimefull")]'
    RESTAURANT_DELIVERY_COST_ENDING = '//div[contains(@class, "delivery-cost")]'
    HEART_ICON = Locator(By.CSS_SELECTOR, '.favorite-icon')
    INFO_ICON = Locator(By.CSS_SELECTOR, '.info-icon')
    DELIVERY_COST = Locator(By.CSS_SELECTOR, '[id="delivery-cost"]')
    KITCHENS_ENDING = '//div[contains(@class, "kitchens")]'
    CLOSE_MODAL = Locator(By.CSS_SELECTOR, '.tabs-header__modal-close')


class MenuModalLocators:
    FAVORITES_TAB = Locator(By.CSS_SELECTOR, '.js-my-favorites-menu')
    FAVOURITE_RESTAURANT_BY_NAME = Locator(
        By.XPATH,
        '//div[contains(@class, "restaurant")]//h2[normalize-space(text())="{}"]'
    )
    DELIVERY_TIME_ENDING = '//..//div[contains(@class, "avgdeliverytime")]'
    DELIVER_COST_ENDING = '//..//div[contains(@class, "delivery-cost")]'
    KITCHENS_ENDING = '//..//div[contains(@class, "kitchens")]'
    DELETE_ICON = '//..//span[contains(@class, "removefavorite")]'


