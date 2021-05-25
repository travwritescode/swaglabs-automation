"""
These tests cover adding items to the cart in Swag Labs
"""

import random
from pages.products import SwagLabsProducts
from pages.cart import SwagLabsCart


def test_add_items_to_cart(browser, login_user):
    # Given the user is on the Swag Labs products page
    products_page = SwagLabsProducts(browser)

    # When the user adds products to the cart
    list_of_product_indexes = random_inventory_items()
    for i in list_of_product_indexes:
        products_page.add_inventory_item_to_cart_by_index(i)

        # Then the products' button changes to "Remove From Cart"
        assert products_page.get_inventory_item_remove_button(i) \
                   .text \
                   .lower() == 'remove'

    # And the cart badge number reflects the number of items in the cart
    assert int(products_page.get_cart_badge().text) == \
           len(list_of_product_indexes)


def test_remove_items_from_cart_products_page(browser, login_user):
    # Given the user is on the Swag Labs products page
    products_page = SwagLabsProducts(browser)

    # And the user has added items to their cart
    list_of_product_indexes = random_inventory_items()
    for i in list_of_product_indexes:
        products_page.add_inventory_item_to_cart_by_index(i)

        # When the user clicks the "Remove" button
        products_page.get_inventory_item_remove_button(i).click()

        # Then the item is removed from their cart
        assert products_page. \
                   get_inventory_item_add_to_cart_button_by_index(i). \
                   text. \
                   lower() == 'add to cart'
    assert products_page.cart_badge_does_not_exist()


def test_remove_items_from_cart_cart_page(browser, login_user):
    products_page = SwagLabsProducts(browser)
    cart_page = SwagLabsCart(browser)

    # Given the user has added items to their cart
    items_in_cart = {}
    list_of_product_indexes = random_inventory_items()
    for i in list_of_product_indexes:
        items_in_cart.update(
            products_page.add_inventory_item_to_cart_by_index(i))

    # And the user is on the cart page
    products_page.open_shopping_cart().click()
    assert cart_page.cart_page_title().text.lower() == 'your cart'

    # When the user clicks "Remove" on an item
    cart_page.remove_cart_items()

    # Then the item is removed from the cart
    assert cart_page.is_cart_empty()


def test_continue_shopping(browser, login_user):
    products_page = SwagLabsProducts(browser)
    cart_page = SwagLabsCart(browser)

    # Given the user is on the cart page
    list_of_product_indexes = random_inventory_items()
    for i in list_of_product_indexes:
        products_page.add_inventory_item_to_cart_by_index(i)
    number_of_items_in_cart = int(products_page.get_cart_badge().text)
    products_page.open_shopping_cart().click()

    # When the user clicks the Continue Shopping button
    cart_page.click_continue_shopping_button()

    # Then the user is returned to the inventory page
    assert products_page.title().lower() == 'products'

    # And the cart remains the same
    assert int(products_page.get_cart_badge().text) == number_of_items_in_cart


def random_inventory_items():
    number_of_items = random.randint(1, 6)

    item_numbers = []
    for i in range(0, number_of_items):
        item_numbers.append(random.randint(0, 5))
    return set(item_numbers)
