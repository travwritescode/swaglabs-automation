"""
These tests cover adding items to the cart in Swag Labs
"""

import random
from pages.products import SwagLabsProducts


def test_add_items_to_cart(browser, login_user):

    # Given the user is on the Swag Labs products page
    products_page = SwagLabsProducts(browser)

    # When the user adds products to the cart
    list_of_product_indexes = random_inventory_items()
    for i in list_of_product_indexes:
        products_page.add_inventory_item_to_cart(i).click()

        # Then the products' button changes to "Remove From Cart"
        assert products_page.inventory_item_in_cart(i).text.lower() == 'remove'

    # And the cart badge number reflects the number of items in the cart
    assert int(products_page.cart_badge().text) == len(list_of_product_indexes)


def test_remove_items_from_cart_products_page(browser, login_user):

    # Given the user is on the Swag Labs products page
    products_page = SwagLabsProducts(browser)

    # And the user has added items to their cart
    list_of_product_indexes = random_inventory_items()
    for i in list_of_product_indexes:
        products_page.add_inventory_item_to_cart(i).click()

    # When the user clicks the "Remove" button
        products_page.inventory_item_in_cart(i).click()

    # Then the item is removed from their cart
        assert products_page.add_inventory_item_to_cart(i).text.lower() == 'add to cart'
    assert products_page.cart_badge_does_not_exist()


def test_remove_items_from_cart_cart_page(browser, login_user):

    # Given the user has added items to their cart
    products_page = SwagLabsProducts(browser)

    # And the user is on the cart page
    # TODO Implement cart page model

    # When the user clicks "Remove" on an item

    # Then the item is removed from the cart


def random_inventory_items():
    number_of_items = random.randint(1, 6)

    item_numbers = []
    for i in range(0, number_of_items):
        item_numbers.append(random.randint(0, 5))
    return set(item_numbers)
