"""
This module contains SwagLabsProducts
the page object for the SwagLabs products page
"""

from selenium.webdriver.common.by import By


class SwagLabsProducts:

    # Locators
    TITLE = (By.CLASS_NAME, 'title')
    INVENTORY_ITEM_NAMES = (By.CLASS_NAME, 'inventory_item_name')
    INVENTORY_ITEM_PRICES = (By.CLASS_NAME, 'inventory_item_price')

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def product_names(self):
        product_names = self.browser.find_elements(*self.INVENTORY_ITEM_NAMES)
        names = [product.text for product in product_names]
        return names

    def product_prices(self):
        product_prices = self.browser.find_elements(*self.INVENTORY_ITEM_PRICES)
        prices = [price.text for price in product_prices]
        return prices

    def title(self):
        title = self.browser.find_element(*self.TITLE)
        return title.text
