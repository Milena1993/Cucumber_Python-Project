Feature: Add Customer on XYZ Bank page

    Scenario: As a bank manager, I can add and delete customer
        Given I'm on XYZ Bank login Page
        When I login as a bank manager and I click on "Add Customer" button 
        And  I fill up all the required fields and click on "Add Customer" button
        Then The success alert asserting  customer adding is displayed
        And I search the new created customer by any parameter
        Then The customer details are displayed
        And I delete the customer by click on "Delete" button
        Then The customer information is deleted
