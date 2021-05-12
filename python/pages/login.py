"""
This module contains SwagLabsLoginPage,
the page object for the SwagLabs login page.
"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class SwagLabsLoginPage:

    # Locators
    URL = 'https://www.saucedemo.com/'
    USER_INPUT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    LOGIN_ERROR = (By.CLASS_NAME, 'error-button')

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def load(self):
        self.browser.get(self.URL)

    def login(self, username, password):
        user_input = self.browser.find_element(*self.USER_INPUT)
        user_input.send_keys(username)
        password_input = self.browser.find_element(*self.PASSWORD_INPUT)
        password_input.send_keys(password)
        login_button = self.browser.find_element(*self.LOGIN_BUTTON)
        login_button.click()

    def error_button_text(self):
        # TODO Implement a smart wait for the error text
        error = self.browser.find_element(*self.LOGIN_ERROR)
        return error.text

    def error_button_exists(self):
        # TODO implement a smart wait for the error to exist
        try:
            self.browser.find_element(*self.LOGIN_ERROR)
        except NoSuchElementException:
            return False
        return True
