"""
This module contains SwagLabsCheckout
the page model for the checkout page
"""

from selenium.webdriver.common.by import By
import re


def strip_non_price_characters(s):
    return re.sub("[^0-9^.]", "", s)


class SwagLabsCheckout:
    # Locators
    CHECKOUT_PAGE_TITLE = (By.CLASS_NAME, 'title')
    INPUT_FIRST_NAME = (By.ID, 'first-name')
    INPUT_LAST_NAME = (By.ID, 'last-name')
    INPUT_POSTAL_CODE = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    CART_ITEM = (By.CLASS_NAME, 'cart_item')
    CART_ITEM_TITLE = (By.XPATH, './/div[@class="inventory_item_name"]')
    CART_ITEM_PRICE = (By.XPATH, './/div[@class="inventory_item_price"]')
    SUBTOTAL = (By.CLASS_NAME, 'summary_subtotal_label')
    TAX = (By.CLASS_NAME, 'summary_tax_label')
    TOTAL = (By.CLASS_NAME, 'summary_total_label')
    COMPLETE_TRANSACTION_BUTTON = (By.ID, 'finish')
    COMPLETED_TRANSACTION_MESSAGE = (By.CLASS_NAME, 'complete-header')
    BACK_HOME_BUTTON = (By.ID, 'back-to-products')

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def checkout_page_title(self):
        return self.browser.find_element(*self.CHECKOUT_PAGE_TITLE)

    def fill_personal_information(self, first_name, last_name, postal_code):
        input_first_name = self.browser.find_element(*self.INPUT_FIRST_NAME)
        input_last_name = self.browser.find_element(*self.INPUT_LAST_NAME)
        input_postal_code = self.browser.find_element(*self.INPUT_POSTAL_CODE)

        input_first_name.send_keys(first_name)
        input_last_name.send_keys(last_name)
        input_postal_code.send_keys(postal_code)

    def click_continue_button(self):
        continue_button = self.browser.find_element(*self.CONTINUE_BUTTON)

        continue_button.click()

    def get_cart_items(self):
        name_and_price = {}
        cart_items = self.browser.find_elements(*self.CART_ITEM)

        # TODO Figure out why the price div is not being found by Selenium
        for item in cart_items:
            print(item.find_element(*self.CART_ITEM_TITLE))
            print(item.find_element(*self.CART_ITEM_PRICE))
            name_and_price[item.find_element(*self.CART_ITEM_TITLE).text] = \
                strip_non_price_characters(
                    item.find_element(*self.CART_ITEM_PRICE).text
                )

        return name_and_price

    def get_subtotal_amount(self):
        subtotal = self.browser.find_element(*self.SUBTOTAL).text
        stripped_subtotal = strip_non_price_characters(subtotal)

        return stripped_subtotal

    def get_tax_amount(self):
        tax_amount = self.browser.find_element(*self.TAX).text
        stripped_tax_amount = strip_non_price_characters(tax_amount)

        return stripped_tax_amount

    def get_total_amount(self):
        total = self.browser.find_element(*self.TOTAL).text
        stripped_total = strip_non_price_characters(total)

        return stripped_total

    def complete_transaction(self):
        finish_button = self.browser.find_element(
            *self.COMPLETE_TRANSACTION_BUTTON
        )

        finish_button.click()

    def get_transaction_complete_message(self):
        transaction_complete_message = self.browser.find_element(
            *self.COMPLETED_TRANSACTION_MESSAGE
        )

        return transaction_complete_message.text.lower()

    def return_home(self):
        return_home_button = self.browser.find_element(*self.BACK_HOME_BUTTON)

        return_home_button.click()
