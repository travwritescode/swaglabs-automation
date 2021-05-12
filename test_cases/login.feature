Scenario: SwagLabs Standard Login
  Given the SwagLabs login page is displayed
  When the user enters a valid username and password
  Then the user successfully logs in
  And the products page is displayed

Scenario: SwagLabs failed login
  Given the SwagLabs login page is displayed
  When the user enters an invalid username or password
  Then the user cannot log in
  And an error message is displayed on the login page

Scenario: Locked out user tries to log in
  Given the SwagLabs login page is displayed
  When the user enters the locked out user's username and password
  Then the user is not logged in
  And an error message is displayed on the login page indicating the user is locked out