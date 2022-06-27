from pages.delete_user import DeleteUser
from utilities.conftest import setup, config
from pages.login_page import LoginPage
from pages.add_user import AddUser
from pages.search_user import Customerpage
from pytest_bdd import scenario, given, when, then
import pytest
import time

@scenario('../features/cucumber.feature', 'As a bank manager, I can add and delete customer')


@given("I'm on XYZ Bank login Page")
def test_add_cutsomer_flow(setup):
    loginPage = LoginPage(setup)
    actual_result = loginPage.get_page_title()
    expected_result = loginPage.page_title
    assert actual_result == expected_result
    
@when("I login as a bank manager and I click on Add Customer button")
def login(setup):
    loginPage = LoginPage(setup)
    loginPage.bank_manager_login()

@when("I fill up all the required fields and click on Add Customer button")
@when("I search the new created customer by any parameter")
@then("I assert that the customer is added with correct info")
def add_search_customer(setup):
    addUser = AddUser(setup)
    first_name = addUser.add_customer_firstname()
    last_name = addUser.add_customer_lastname()
    postal_code = addUser.add_customer_postcode()
    customerPage = Customerpage(setup)
    customerPage.search_customers(first_name)
    assert first_name == customerPage.table_firstname()
    assert last_name == customerPage.table_lastname()
    assert postal_code == customerPage.table_postcode()
   

@when("I delete the customer by click on Delete button")
@then("I assert that the customer information is deleted")
def delete_customer(setup):
    deleteUser = DeleteUser(setup)
    deleteUser.delete_customer()
    assert deleteUser.table_existing_check() == None
  
    
