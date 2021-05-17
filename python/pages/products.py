"""
This module contains SwagLabsProducts
the page object for the SwagLabs products page
"""

from selenium.webdriver.common.by import By


class SwagLabsProducts:

    # Locators
    TITLE = (By.CLASS_NAME, 'title')
    INVENTORY_ITEM_CARDS = (By.CLASS_NAME, 'inventory_item')
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, 'inventory_item_name')
    INVENTORY_ITEM_PRICE = (By.CLASS_NAME, 'inventory_item_price')
    INVENTORY_ADD_TO_CART = (By.XPATH, '//button[contains(@id, "add-to-cart-")]')
    INVENTORY_REMOVE_FROM_CART = (By.XPATH, '//button[contains(@id, "remove-")]')

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def product_names(self):
        product_names = self.browser.find_elements(*self.INVENTORY_ITEM_NAME)
        names = [product.text for product in product_names]
        return names

    def product_prices(self):
        product_prices = self.browser.find_elements(*self.INVENTORY_ITEM_PRICE)
        prices = [price.text for price in product_prices]
        return prices

    def add_inventory_item_to_cart(self, index):
        name_and_price = {}
        inventory_item = self.browser.find_elements(*self.INVENTORY_ITEM_CARDS)[index]

        # Debug
        print(inventory_item.find_element(*self.INVENTORY_ITEM_NAME).text)

        add_to_cart_button = inventory_item.find_element(*self.INVENTORY_ADD_TO_CART)
        add_to_cart_button.click()
        name_and_price[inventory_item.find_element(*self.INVENTORY_ITEM_NAME).text] \
            = inventory_item.find_element(*self.INVENTORY_ITEM_PRICE).text

        return name_and_price

    def title(self):
        title = self.browser.find_element(*self.TITLE)
        return title.text
