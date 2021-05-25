"""
This module contains SwagLabsCart
the page model object for the cart when checking out
"""
from selenium.webdriver.common.by import By


class SwagLabsCart:
    # Locators
    CART_PAGE_TITLE = (By.CLASS_NAME, 'title')
    CART_ITEM = (By.CLASS_NAME, 'cart_item')
    CART_ITEM_TITLE = (By.XPATH, './/div[class="inventory_item_name"]')
    CART_ITEM_PRICE = (By.XPATH, './/div[class="inventory_item_price"]')
    CART_ITEM_REMOVE_FROM_CART = \
        (By.XPATH, './/button[contains(@id, "remove-")]')
    CONTINUE_SHOPPING_BUTTON = (By.ID, 'continue-shopping')

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def cart_page_title(self):
        return self.browser.find_element(*self.CART_PAGE_TITLE)

    def remove_cart_items(self):
        cart_items = self.browser.find_elements(*self.CART_ITEM)

        for item in cart_items:
            item.find_element(*self.CART_ITEM_REMOVE_FROM_CART).click()

    def get_cart_items(self):
        name_and_price = {}
        cart_items = self.browser.find_elements(*self.CART_ITEM)

        for item in cart_items:
            name_and_price[item.find_element(*self.CART_PAGE_TITLE).text] = \
                item.find_element(*self.CART_ITEM_PRICE).text

        return name_and_price

    def is_cart_empty(self):
        cart_items = self.browser.find_elements(*self.CART_ITEM)
        if len(cart_items) == 0:
            return True
        else:
            return False

    def click_continue_shopping_button(self):
        continue_shopping_button = self.browser.find_element(
            *self.CONTINUE_SHOPPING_BUTTON)

        continue_shopping_button.click()
