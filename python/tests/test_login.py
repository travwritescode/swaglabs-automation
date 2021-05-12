"""
These tests cover the SwagLabs login
"""

import pytest
from pages.login import SwagLabsLoginPage
from pages.products import SwagLabsProducts


def test_login(browser):

    login_page = SwagLabsLoginPage(browser)
    products_page = SwagLabsProducts(browser)

    # Given the SwagLabs login page is displayed
    login_page.load()

    # When the user enters a valid username and password
    login_page.login('standard_user', 'secret_sauce')

    # Then the user successfully logs in
    assert products_page.title().lower() == 'products'

    # And the products page is displayed
    assert len(products_page.product_names()) == 6


@pytest.mark.parametrize('username,password',
                         [('incorrect_user', 'secret_sauce'), ('standard_user', 'special_sauce')])
def test_incorrect_login(browser, username, password):
    login_page = SwagLabsLoginPage(browser)

    # Given the SwagLabs login page is displayed
    login_page.load()

    # When the user enters an invalid username or password
    login_page.login(username, password)

    # Then the user cannot log in
    assert login_page.error_button_exists()

    # And an error message is displayed on the login page
    assert 'epic sadface' in login_page.error_button_text()