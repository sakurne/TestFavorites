# Created by Zhanna at 23.02.2021
Feature: #Enter feature name here
  # Enter feature description here

  Scenario: Adding opened restaurant with free delivery to favorites
    Given Currently selected country is Germany
    And Opened restaurants list for address: Munich Central Station, Bayerstraße, Munich
    When Click on any opened restaurant
    And Click on heart icon
    And Click on options icon (top right corner)
    And Choose “favourites”
    Then Restaurant is present on the page
	And Restaurant’s estimated delivery time coincides with the info on presented on the restaurants list
	And Restaurant’s delivery cost coincides with the info on presented on the restaurants list

    Scenario: Adding closed restaurant to favorites
      Given	Opened restaurants list for delivery/pickup
      When Click on closed restaurant which has delivery cost
      And Click on heart icon
      And Click on options icon (top right corner)
      And Choose “favourites”
      Then Restaurant is present on the page
      And Restaurant’s status is “Closed”
      And Restaurant’s delivery cost is just like on the restaurant’s page
      Then Go to main page
      And In search field enter any address where deleted restaurant can be found
      And Expected result: In the list of restaurants there is “favourite” mark next to restaurant which was added to favorites

