"""
These tests cover checkout
"""

from pages.products import SwagLabsProducts
from pages.cart import SwagLabsCart
from pages.checkout import SwagLabsCheckout
from tests.test_cart import random_inventory_items


def test_checkout(browser, login_user):

    products_page = SwagLabsProducts(browser)
    cart_page = SwagLabsCart(browser)
    checkout_page = SwagLabsCheckout(browser)

    # Given the customer has added at least one item to their cart
    items_in_cart = {}
    list_of_product_indexes = random_inventory_items()
    for i in list_of_product_indexes:
        items_in_cart.update(
            products_page.add_inventory_item_to_cart_by_index(i))

    # And the customer is on the cart page
    products_page.open_shopping_cart().click()

    # When the customer clicks the checkout button
    cart_page.click_checkout_button()

    # Then they are prompted to fill in their personal information
    assert checkout_page.checkout_page_title().text.lower() == \
           'checkout: your information'
    checkout_page.fill_personal_information('Test', 'Customer', '55555')

    # When the customer clicks the continue button
    checkout_page.click_continue_button()

    # Then a checkout overview confirmation page is displayed
    assert checkout_page.checkout_page_title().text.lower() == \
           'checkout: overview'

    #  And all information about products and pricing looks correct
    items_at_checkout = checkout_page.get_cart_items()
    cart_prices = [float(i) for i in items_in_cart.values()]
    assert items_at_checkout == items_in_cart
    assert round(float(checkout_page.get_subtotal_amount()), 2) == \
           sum(cart_prices)
    assert float(checkout_page.get_total_amount()) == sum(cart_prices) + \
           float(checkout_page.get_tax_amount())

    # When the customer clicks the finish button
    checkout_page.complete_transaction()

    # Then a thank you message is displayed on the checkout complete page
    assert checkout_page.checkout_page_title().text.lower() == \
           'checkout: complete!'
    assert checkout_page.get_transaction_complete_message() == \
           'thank you for your order'

    # When the customer clicks the back home button
    checkout_page.return_home()

    # Then they are returned to the products page
    assert products_page.get_title().lower() == 'products'
