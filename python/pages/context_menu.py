"""
This module contains SwagLabsContextMenu
the page object for the burger menu on all logged in pages
"""

from selenium.webdriver.common.by import By


class SwagLabsContextMenu:

    # Locators
    MENU_BUTTON = (By.ID, 'react-burger-menu-btn')
    LOGOUT_BUTTON = (By.ID, 'logout_sidebar_link')

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def logout(self):
        hamburger_menu_button = self.browser.find_element(*self.MENU_BUTTON)
        hamburger_menu_button.click()
        logout_button = self.browser.find_element(*self.LOGOUT_BUTTON)
        logout_button.click()
