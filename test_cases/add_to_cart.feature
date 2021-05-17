Scenario: Customer can add items to the cart in Swag Labs
  Given the user is on the Swag Labs products page
  When the user adds products to the cart
  Then the products' button changes to "Remove From Cart"
  And the cart badge number reflects the number of items in the cart