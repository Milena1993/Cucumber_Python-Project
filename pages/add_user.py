from selenium.webdriver.common.by import By
# from pages.search_customer import Customerpage
from faker import Faker

class AddUser:
    firstname_input_field = (By.XPATH, '//input[@placeholder = "First Name"]') 
    lastname_input_field = (By.XPATH, '//input[@placeholder = "Last Name"]') 
    postalcode_input_field = (By.XPATH,'//input[@placeholder = "Post Code"]') 
    add_customer_submit_button = (By.XPATH, '//button[@class = "btn btn-default"]')
    alert_message = 'Customer added successfully with customer id'

    def __init__(self, driver):
        super().__init__()
        self.driver = driver 

    def add_customer_firstname(self):
        fake = Faker()
        first_name = fake.first_name()
        # self.driver.find_element(*AddUser.firstname_input_field).send_keys(*AddUser.firstname)
        self.driver.find_element(*AddUser.firstname_input_field).send_keys(first_name)
        return first_name

    def add_customer_lastname(self):
        fake = Faker()
        last_name = fake.last_name()
        self.driver.find_element(*AddUser.lastname_input_field).send_keys(last_name)
        return last_name

    def add_customer_postcode(self): 
        fake = Faker()
        postal_code  = fake.postcode()
        self.driver.find_element(*AddUser.postalcode_input_field ).send_keys(postal_code)
        self.driver.find_element(*AddUser.add_customer_submit_button).click()
        self.driver.switch_to.alert.accept()
        return postal_code
   

    # def alert(self):
        
    #     # print(alert.text)
    #     # alert.accept()
 
        
      


    
   




        