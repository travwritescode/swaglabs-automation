"""
This module contains SwagLabsProducts
the page object for the SwagLabs products page
"""

import re
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def strip_non_price_characters(s):
    return re.sub("[^0-9^.]", "", s)


class SwagLabsProducts:
    # Locators
    TITLE = (By.CLASS_NAME,
             'title')
    INVENTORY_ITEM_CARDS = (By.CLASS_NAME,
                            'inventory_item')
    INVENTORY_ITEM_NAME = (By.CLASS_NAME,
                           'inventory_item_name')
    INVENTORY_ITEM_PRICE = (By.CLASS_NAME,
                            'inventory_item_price')
    INVENTORY_ADD_TO_CART = (By.XPATH,
                             './/button[contains(@id, "add-to-cart-")]')
    INVENTORY_REMOVE_FROM_CART = (By.XPATH,
                                  './/button[contains(@id, "remove-")]')
    SHOPPING_CART_BADGE = (By.CLASS_NAME,
                           'shopping_cart_badge')
    SHOPPING_CART_LINK = (By.CLASS_NAME,
                          'shopping_cart_link')

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def get_product_names(self):
        product_names = self.browser.find_elements(*self.INVENTORY_ITEM_NAME)
        names = [product.text for product in product_names]
        return names

    def get_product_prices(self):
        product_prices = self.browser.find_elements(*self.INVENTORY_ITEM_PRICE)
        prices = [price.text for price in product_prices]
        return prices

    def get_inventory_item(self, index):
        return self.browser.find_elements(*self.INVENTORY_ITEM_CARDS)[index]

    def add_inventory_item_to_cart(self, index):
        name_and_price = {}
        inventory_item = self.get_inventory_item(index)

        add_to_cart_button = inventory_item.find_element(
            *self.INVENTORY_ADD_TO_CART)
        add_to_cart_button.click()

        name_and_price[
            inventory_item.find_element(*self.INVENTORY_ITEM_NAME).text] = \
            strip_non_price_characters(
                inventory_item.find_element(*self.INVENTORY_ITEM_PRICE).text
            )

        return name_and_price

    def get_inventory_item_add_to_cart_button_text(self, index):
        inventory_item = self.get_inventory_item(index)

        add_to_cart_button = inventory_item.find_element(
            *self.INVENTORY_ADD_TO_CART)
        return add_to_cart_button.text

    def get_inventory_item_remove_from_cart_button_text(self, index):
        inventory_item = self.get_inventory_item(index)

        remove_button = inventory_item.find_element(
            *self.INVENTORY_REMOVE_FROM_CART)
        return remove_button.text

    def remove_inventory_item_from_cart(self, index):
        inventory_item = self.get_inventory_item(index)

        remove_button = inventory_item.find_element(
            *self.INVENTORY_REMOVE_FROM_CART)
        remove_button.click()

    def open_shopping_cart(self):
        return self.browser.find_element(*self.SHOPPING_CART_LINK).click()

    def get_cart_badge_number(self):
        return self.browser.find_element(*self.SHOPPING_CART_BADGE).text

    def cart_badge_does_not_exist(self):
        try:
            self.browser.find_element(*self.SHOPPING_CART_BADGE)
            return False
        except NoSuchElementException:
            return True

    def get_title(self):
        title = self.browser.find_element(*self.TITLE)
        return title.text
