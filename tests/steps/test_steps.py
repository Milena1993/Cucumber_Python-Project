from pages.delete_user import DeleteUser
from utilities.conftest import setup, config
from pages.login_page import LoginPage
from pages.add_user import AddUser
from pages.search_user import Customerpage
from pytest_bdd import scenario, given, when, then
import pytest
import time


@pytest.mark.usefixtures('setup', 'config')
class Test():



    # @scenario('features/cucumber.feature', 'As a bank manager, I can add and delete customer')

    
    # @given('Im on XYZ Bank login Page')
    def test_add_cutsomer_flow(self):
        actual_result = LoginPage.get_page_title(self)
        expected_result = LoginPage.page_title
        assert actual_result == expected_result
        
    # @when('I login as a bank manager and I click on "Add Customer" button ')
    # def test_login(self):
        loginPage = LoginPage(self.driver)
        loginPage.bank_manager_login()

    # @when('I fill up all the required fields and click on "Add Customer" button')
    # def test_add_customer(self):
        addUser = AddUser(self.driver)
        first_name = addUser.add_customer_firstname()
        last_name = addUser.add_customer_lastname()
        postal_code = addUser.add_customer_postcode()
        
        
    # @when('I search the new created customer by any parameter')
    # @then('I assert that the customer is added with correct info')
    # def search_customer(self):
        customerPage = Customerpage(self.driver)
        customerPage.search_customers(first_name)
        assert first_name == customerPage.table_firstname()
        assert last_name == customerPage.table_lastname()
        assert postal_code == customerPage.table_postcode()
       
    
    # @when('I delete the customer by click on "Delete" button')
    # @then('I assert that the customer information is deleted')
    # def search_customer(self):
        deleteUser = DeleteUser(self.driver)
        deleteUser.delete_customer()
        assert deleteUser.table_existing_check() == None
        time.sleep(2)
        
