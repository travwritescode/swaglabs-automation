"""
These tests cover adding items to the cart in Swag Labs
"""

import pytest
import random
from pages.products import SwagLabsProducts
from pages.login import SwagLabsLoginPage


@pytest.fixture()
def login_user(browser):

    # TODO move this fixture into a shared file for all tests
    login_page = SwagLabsLoginPage(browser)

    # Log in user for test
    login_page.load()
    login_page.login('standard_user', 'secret_sauce')

    # TODO add cleanup to the fixture to reset app state at the end of tests


def test_add_items_to_cart(browser, login_user):

    products_page = SwagLabsProducts(browser)

    # Given the user is on the Swag Labs products page
    # When the user adds products to the cart
    list_of_product_indexes = random_inventory_items()

    # Debug
    print(list_of_product_indexes)

    product_dict = {}
    for i in list_of_product_indexes:
        product_dict.update(products_page.add_inventory_item_to_cart(i))

    # Then the products' button changes to "Remove From Cart"
    # TODO Add verification of button change for each item

    # And the cart badge number reflects the number of items in the cart
    # TODO Add verification of cart badge

    # Manual Inspection for debugging
    # import time
    # time.sleep(10)


def random_inventory_items():
    number_of_items = random.randint(1, 6)

    # Debug
    print(number_of_items)

    item_numbers = []
    for i in range(0, number_of_items):
        item_numbers.append(random.randint(0, 5))
    return set(item_numbers)
