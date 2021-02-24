from pytest_bdd import when, then, given, scenarios
from pytest_bdd import parsers
from settings import global_settings
from pages.main_page import MainPage

scenarios('../features/favorites.feature')

COUNTRIES = {
    'Germany': global_settings.GERMANY_MAIN_PAGE,
    'Netherlands': global_settings.NETHERLANDS_MAIN_PAGE,
    'Belgium': global_settings.BELGIUM_MAIN_PAGE,
    'Poland': global_settings.POLAND_MAIN_PAGE,
    'Austria': global_settings.AUSTRIA_MAIN_PAGE,
    'Switzerland': global_settings.SWITZERLAND_MAIN_PAGE,
    'Luxembourg': global_settings.LUXEMBOURG_MAIN_PAGE,
    'Portugal': global_settings.PORTUGAL_MAIN_PAGE
}


@given(parsers.cfparse('Currently selected country is {country_name}'))
def selected_country_is(app_function, country_name):
    app_function.current_page = MainPage(app_function, COUNTRIES.get(country_name))


@given(parsers.cfparse('Opened restaurants list for address: {address}'))
def opened_restaurants_page(app_function, address):
    app_function.current_page.search_address(address)


@when('Click on any opened restaurant')
def click_any_opened_restaurant(app_function):
    app_function.current_page.click_any_restaurant(opened=True)


@when('Click on heart icon')
def click_heart_icon(app_function):
    app_function.current_page.click_heart_icon()


@when('Click on options icon (top right corner)')
def click_options(app_function):
    app_function.current_page.click_options()


@when('Choose “favourites”')
def click_options(app_function):
    app_function.current_page.click_favorites()


@then('Restaurant is present on the page')
def restaurant_is_present(app_function):
    app_function.current_page.restaurant_is_present()


@then('Restaurant’s estimated delivery time coincides with the info on presented on the restaurants list')
def compare_delivery_time(app_function):
    app_function.current_page.compare_delivery_time()


@then('Restaurant’s delivery cost coincides with the info on presented on the restaurants list')
def compare_delivery_cost(app_function):
    app_function.current_page.compare_delivery_cost()
