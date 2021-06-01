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
    assert products_page.get_title().lower() == 'products'

    # And the products page is displayed
    assert len(products_page.get_product_names()) == 6


@pytest.mark.parametrize('username,password',
                         [('incorrect_user', 'secret_sauce'),
                          ('standard_user', 'special_sauce')])
def test_incorrect_login(browser, username, password):

    login_page = SwagLabsLoginPage(browser)

    # Given the SwagLabs login page is displayed
    login_page.load()

    # When the user enters an invalid username or password
    login_page.login(username, password)

    # Then the user cannot log in
    assert login_page.error_exists()

    # And an error message is displayed on the login page
    assert 'Username and password do not match any user in this service' \
           in login_page.get_error_message()


def test_locked_out_user(browser):

    login_page = SwagLabsLoginPage(browser)

    # Given the SwagLabs login page is displayed
    login_page.load()

    # When the user enters the locked out user's username and password
    login_page.login('locked_out_user', 'secret_sauce')

    # Then the user is not logged in
    assert login_page.error_exists()

    # And an error message is displayed on the login page indicating the user
    # is locked out
    assert 'Sorry, this user has been locked out.' \
           in login_page.get_error_message()
