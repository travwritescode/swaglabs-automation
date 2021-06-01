"""
These tests cover SwagLabs logout
"""

from pages.login import SwagLabsLoginPage
from pages.context_menu import SwagLabsContextMenu


def test_logout(browser, login_user):

    context_menu = SwagLabsContextMenu(browser)
    login_page = SwagLabsLoginPage(browser)

    # Given the user is logged in to SwagLabs
    # When the user logs out
    context_menu.logout()

    # Then the user is returned to the login screen
    assert login_page.is_loaded()
