from selenium.webdriver.common.by import By
from pages.add_user import AddUser


class Customerpage(AddUser):
    customers_button = (By.XPATH,'//button[@ng-click="showCust()"]')
    search_customer_field = (By.XPATH, '//input[@placeholder = "Search Customer"]')
    t_firstname = (By.CSS_SELECTOR, 'tbody>tr>td:nth-child(1)') #under improvement :) 
    t_lastname = (By.CSS_SELECTOR, 'tbody>tr>td:nth-child(2)') #under improvement :) 
    t_postcode = (By.CSS_SELECTOR, 'tbody>tr>td:nth-child(3)') #under improvement :) 

 
    def search_customers(self, locator):
        self.driver.find_element(*Customerpage.customers_button).click()
        search_field = self.driver.find_element(*Customerpage.search_customer_field)
        search_field.clear()
        search_field.send_keys(locator)
        return search_field.get_attribute("value")

    def table_firstname(self):
        return self.driver.find_element(*Customerpage.t_firstname).text
        
    def table_lastname(self):
        return self.driver.find_element(*Customerpage.t_lastname).text

    def table_postcode(self):
        return self.driver.find_element(*Customerpage.t_postcode).text
        
  


