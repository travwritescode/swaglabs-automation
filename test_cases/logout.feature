Scenario: User can safely log out of SwagLabs
  Given the user is logged in to SwagLabs
  When the user logs out
  Then the user is returned to the login screen