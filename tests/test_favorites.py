from pytest_bdd import when, then, given, scenarios
from pytest_bdd import parsers
# from fixtures.function_fixtures import *
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
    app_function.current_page = MainPage(COUNTRIES.get(country_name))
