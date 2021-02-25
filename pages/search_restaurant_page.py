from pages.base_page import BasePage
from pages.menu_modal import MenuModal
from locators import SearchRestaurantLocators as Locs
from locators import BaseLocators as BaseLocs
import re
import random
import pytest


class ChosenRestaurant:
    def __init__(self):
        self.name = None
        self.delivery_time = None
        self.delivery_cost = None


class SearchRestaurantPage(BasePage):
    def __init__(self, app):
        super(SearchRestaurantPage, self).__init__(app)

    def click_any_restaurant(self, opened=False, preorder=False, closed=False, any=False):
        if [opened, preorder, closed, any].count(True) != 1:
            raise Exception(' 1 type of restaurants should be chosen')
        self.app.chosen_restaurant = ChosenRestaurant()
        if any:
            restaurant_loc = self.get_random(Locs.ALL_RESTAURANTS)
        elif closed:
            restaurant_loc = self.get_random(Locs.RESTURANTS_CLOSED)
        else:
            restaurant_loc = self.get_random(Locs.RESTAURANTS_OPENED) if opened else \
                self.get_random(Locs.RESTAURANTS_PREORDER)
            self.app.chosen_restaurant.delivery_cost = self.get_delivery_cost(restaurant_loc)
            self.app.chosen_restaurant.delivery_time = 'est. ' + self.get_delivery_time(restaurant_loc)
        self.app.chosen_restaurant.name = self.get_name(restaurant_loc)
        self.app.chosen_restaurant.kitchen_types = self.get_kitchen_types(restaurant_loc)
        self.scroll_to_element(*restaurant_loc)
        self.scroll(y='-200')
        self.click_element(*restaurant_loc)
        if closed:
            self.app.chosen_restaurant.delivery_cost = self.get_closed_restaurant_delivery_cost()

    def get_kitchen_types(self, restaurant_loc):
        return self.get_attribute_from_element(
            restaurant_loc[0],
            restaurant_loc[1] + Locs.KITCHENS_ENDING,
            'innerText'
        )

    def get_closed_restaurant_delivery_cost(self):
        self.click_element(*Locs.INFO_ICON)
        delivery_cost = None
        if self.should_be_element(*Locs.DELIVERY_COST):
            delivery_cost = self.get_attribute_from_element(*Locs.DELIVERY_COST, 'innerText')
            if self.search_price(delivery_cost) == '0,00':
                delivery_cost = 'FREE'
        self.click_element(*Locs.CLOSE_MODAL)
        return delivery_cost

    def search_price(self, string):
        return re.search(r'\d+,\d+', string).group(0)

    def get_random(self, locator):
        try:
            random_index = random.randint(
                1,
                self.count_of_elements(
                    *locator
                )
            )
        except AssertionError:
            pytest.skip(
                'There are no restaurants of requested status (opened/closed/preorder). '
                'Try later or input another adderess'
            )
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
