from pages.base_page import BasePage
from locators import MenuModalLocators
from settings import global_settings


class MenuModal(BasePage):
    def __init__(self, app):
        super(MenuModal, self).__init__(app)

    def click_favorites(self):
        self.click_element(*MenuModalLocators.FAVORITES_TAB)

    def get_restaurant_locator(self):
        return MenuModalLocators.FAVOURITE_RESTAURANT_BY_NAME(
            self.app.chosen_restaurant.name
        )

    def restaurant_is_present(self):
        assert self.should_be_element(*self.get_restaurant_locator()), \
            'restaurant {} is not found on the favorites list'.format(self.app.chosen_restaurant.name)

    def restaurant_is_not_present(self):
        assert not self.should_be_element(*self.get_restaurant_locator(), timeout=global_settings.DEFAULT_TIMEOUT/3), \
            'restaurant {} is on the favorites list'.format(self.app.chosen_restaurant.name)

    def click_delete_added_restaurant(self):
        res_locator = self.get_restaurant_locator()
        res_locator = (res_locator[0], res_locator[1] + MenuModalLocators.DELETE_ICON)
        self.click_element(*res_locator)

    def compare_delivery_time(self, text=None):
        res_loc = self.get_restaurant_locator()
        current_value = self.get_attribute_from_element(
            res_loc[0],
            res_loc[1] + MenuModalLocators.DELIVERY_TIME_ENDING,
            'innerText'
        ).strip()
        if text:
            expexted_value = text
        else:
            expexted_value = self.app.chosen_restaurant.delivery_time
        assert current_value == expexted_value, \
            'restaurant delivery time is not correct:\ncurrent - {}\nexpected - {}\nrestaurant - {}'.format(
                current_value,
                expexted_value,
                self.app.chosen_restaurant.name
            )

    def compare_kitchen_types(self):
        res_loc = self.get_restaurant_locator()
        current_value = self.get_attribute_from_element(
            res_loc[0],
            res_loc[1] + MenuModalLocators.KITCHENS_ENDING,
            'innerText'
        ).strip()
        expexted_value = self.app.chosen_restaurant.kitchen_types
        assert current_value == expexted_value, \
            'restaurant kitchen types are not correct:\ncurrent - {}\nexpected - {}\nrestaurant - {}'.format(
                current_value,
                expexted_value,
                self.app.chosen_restaurant.name
            )

    def compare_delivery_cost(self):
        res_loc = self.get_restaurant_locator()
        current_value = self.get_attribute_from_element(
            res_loc[0],
            res_loc[1] + MenuModalLocators.DELIVER_COST_ENDING,
            'innerText'
        ).strip()
        assert current_value == self.app.chosen_restaurant.delivery_cost, \
            'restaurant delivery cost is not correct:\ncurrent - {}\nexpected - {}\nrestaurant - {}'.format(
                current_value,
                self.app.chosen_restaurant.delivery_cost,
                self.app.chosen_restaurant.name
            )
