"""
These tests cover SwagLabs logout
"""

import pytest
from pages.login import SwagLabsLoginPage
from pages.context_menu import SwagLabsContextMenu


@pytest.fixture()
def login_user(browser):

    login_page = SwagLabsLoginPage(browser)

    # Log in user for test
    login_page.load()
    login_page.login('standard_user', 'secret_sauce')


def test_logout(browser, login_user):

    context_menu = SwagLabsContextMenu(browser)
    login_page = SwagLabsLoginPage(browser)

    # Given the user is logged in to SwagLabs

    # When the user logs out
    context_menu.logout()

    # Then the user is returned to the login screen
    assert login_page.verify_page()
