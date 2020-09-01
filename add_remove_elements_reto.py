import unittest
from selenium import webdriver
from time import sleep

class AddRemoveElements_Reto(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Add/Remove Elements').click()

    
    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input('Cuantos elementos desea agregar?: '))

        add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')

        sleep(3)

        for i in range(elements_added):
            add_button.click()

        elements_removed = int(input('cuantos elementos desea remover?: '))

        while elements_removed > elements_added:
        
            for i in range(elements_removed):

                    print("Intentas remover mas elementos de los que ingresaste")

                    if elements_removed > elements_added:

                        elements_removed = int(input('cuantos elementos desea remover?: '))
                        
                        delete_button = driver.find_element_by_xpath('//*[@id="elements"]/button[1]')
                        delete_button.click()
                        break   

        sleep(3)                    
        total_elements = elements_added - elements_removed

        if total_elements == 1:

            print(f'Removiste {elements_removed} elementos, queda {total_elements} elemento')

        elif total_elements > 1 or total_elements < 1:
            
            print(f'Removiste {elements_removed}, quedan {total_elements} elementos')  


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity = 2)