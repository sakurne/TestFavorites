from pages.base_page import BasePage
from pages.menu_modal import MenuModal
from locators import SearchRestaurantLocators as Locs
from locators import BaseLocators as BaseLocs
import random


class ChosenRestaurant:
    def __init__(self):
        self.name=None
        self.delivery_time = None
        self.delivery_cost = None


class SearchRestaurantPage(BasePage):
    def __init__(self, app):
        super(SearchRestaurantPage, self).__init__(app)

    def click_any_restaurant(self, opened=True, preorder=False, closed=False):
        if [opened, preorder, closed].count(True) != 1:
            raise Exception(' 1 type of restaurants should be chosen')
        self.app.chosen_restaurant = ChosenRestaurant()
        if closed:
            restaurant_loc = self.get_random(Locs.RESTURANTS_CLOSED)
        else:
            restaurant_loc = self.get_random(Locs.RESTAURANTS_OPENED) if opened else self.get_random(Locs.RESTAURANTS_PREORDER)
            self.app.chosen_restaurant.delivery_cost = self.get_delivery_cost(restaurant_loc)
            self.app.chosen_restaurant.delivery_time = 'est. ' + self.get_delivery_time(restaurant_loc)
        self.app.chosen_restaurant.name = self.get_name(restaurant_loc)
        self.scroll_to_element(*restaurant_loc)
        self.scroll(y='-200')
        self.click_element(*restaurant_loc)

    def get_random(self, locator):
        random_index = random.randint(1, self.count_of_elements(*locator))
        return (
            locator[0],
            locator[1] + BaseLocs.INDEX_ENDING.format(random_index)
        )

    def get_name(self, restaurant_loc):
        return self.get_attribute_from_element(
            restaurant_loc[0],
            restaurant_loc[1] + Locs.RESTAURANT_NAME_ENDING,
            'innerText'
        )

    def get_delivery_cost(self, restaurant_loc):
        return self.get_attribute_from_element(
            restaurant_loc[0],
            restaurant_loc[1] + Locs.RESTAURANT_DELIVERY_COST_ENDING,
            'innerText'
        )

    def get_delivery_time(self, restaurant_loc):
        return self.get_attribute_from_element(
            restaurant_loc[0],
            restaurant_loc[1] + Locs.RESTAURANT_DELIVERY_TIME_ENDING,
            'innerText'
        )

    def click_heart_icon(self):
        self.click_element(*Locs.HEART_ICON)

    def click_options(self):
        self.click_element(*BaseLocs.OPTIONS_ICON)
        self.app.current_page = MenuModal(self.app)
