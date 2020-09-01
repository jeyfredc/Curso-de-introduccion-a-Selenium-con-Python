import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ExplicitiWaitTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        self.driver.get('http://demo-store.seleniumacademy.com')


    def test_account_link(self):
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_id('select-language').get_attribute('length') == '3')

        account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
        account.click()

    
    def test_create_new_costumer(self):
        self.driver.find_element_by_link_text('ACCOUNT').click()

        my_account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Account')))  
        my_account.click()

        create_account_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
        create_account_button.click()

        WebDriverWait(self.driver, 10).until(EC.title_contains('Create New Customer Account'))


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity = 2)