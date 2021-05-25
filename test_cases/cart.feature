Scenario: Customer can add items to the cart in Swag Labs
  Given the user is on the Swag Labs products page
  When the user adds products to the cart
  Then the products' button changes to "Remove From Cart"
  And the cart badge number reflects the number of items in the cart

Scenario: Customer can remove items from the cart on the Swag Labs products page
  Given the user is on the Swag Labs products page
  And the user has added items to their cart
  When the user clicks the "Remove" button
  Then the item is removed from their cart

Scenario: Customer can remove items from the cart on the Swag Labs cart page
  Given the user has added items to their cart
  And the user is on the cart page
  When the user clicks "Remove" on an item
  Then the item is removed from the cart

Scenario: Customer can return to the inventory page from the cart page
  Given the user is on the cart page
  When the user clicks the Continue Shopping button
  Then the user is returned to the inventory page