Feature: Add Customer
    Scenario: As a bank manager, I can add and delete customer
        Given I'm on XYZ Bank login Page
        When I login as a bank manager and I click on Add Customer button 
        And I fill up all the required fields and click on Add Customer button
        When I search the new created customer by any parameter
        Then I assert that the customer is added with correct info
        When I delete the customer by click on Delete button
        Then I assert that the customer information is deleted
