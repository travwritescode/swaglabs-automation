Scenario: Customer can checkout with their cart from the Swag Labs store
  Given the customer has added at least one item to their cart
  And the customer is on the cart page
  When the customer clicks the checkout button
  Then they are prompted to fill in their personal information
  When the customer clicks the continue button
  Then a checkout overview confirmation page is displayed
  When the customer clicks the finish button
  Then a thank you message is displayed on the checkout complete page
  When the customer clicks the back home button
  Then they are returned to the products page