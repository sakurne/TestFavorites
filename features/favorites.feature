Feature: Favorite restaurants

  Scenario: Adding opened restaurant with free delivery to favorites
    Given Currently selected country is Germany
    And Opened restaurants list for address: Munich Central Station, Bayerstraße, Munich
    When Click on any opened restaurant
    And Click on heart icon
    And Click on options icon (top right corner)
    And Choose “favourites”
    Then Restaurant is present on the page
    And Restaurant’s estimated delivery time coincides with the info on presented on the restaurants list
    And Restaurant’s kitchen types are just like on the restaurant’s page
    And Restaurant’s delivery cost coincides with the info on presented on the restaurants list

  Scenario: Adding closed restaurant to favorites
    Given Currently selected country is Germany
    And Opened restaurants list for address: Munich Central Station, Bayerstraße, Munich
    When Click on any closed restaurant
    And Click on heart icon
    And Click on options icon (top right corner)
    And Choose “favourites”
    Then Restaurant is present on the page
    And Restaurant’s status is “Closed”
    And Restaurant’s delivery cost coincides with the info on presented on the restaurants list

  Scenario: Adding restaurant with preorder to favorites
    Given Currently selected country is Germany
    And Opened restaurants list for address: Munich Central Station, Bayerstraße, Munich
    When Click on any restaurant with preorder
    And	Click on heart icon
    And	Click on options icon (top right corner)
    And	Choose “favourites”
    Then Restaurant is present on the page
    And	Restaurant’s estimated delivery time coincides with the info on presented on the restaurants list

   Scenario: Deleting restaurant from favorites
     Given Currently selected country is Germany
     And Opened restaurants list for address: Munich Central Station, Bayerstraße, Munich
     Given Favorites list is not empty
     When Click on options icon (top right corner)
     And Choose “favourites”
     And Click on delete button next to the restaurant
     Then Restaurant is not present on the list
