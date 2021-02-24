from pages.base_page import BasePage
from locators import MenuModalLocators


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
        assert self.should_be_element(*self.get_restaurant_locator()), 'restaurant is not found'

    def compare_delivery_time(self):
        res_loc = self.get_restaurant_locator()
        current_value = self.get_attribute_from_element(
            res_loc[0],
            res_loc[1] + MenuModalLocators.DELIVERY_TIME_ENDING,
            'innerText'
        ).strip()
        assert current_value == self.app.chosen_restaurant.delivery_time, \
            'restaurant delivery time is not correct:\ncurrent - {}\nexpected - {}\nrestaurant - {}'.format(
                current_value,
                self.app.chosen_restaurant.delivery_time,
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
