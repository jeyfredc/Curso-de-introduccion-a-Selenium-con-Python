import unittest

from selenium import webdriver

class SearchTests(unittest.TestCase):
    

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= './chromedriver')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)


    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()


    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')

        search_field.send_keys('salt shaker')
        search_field.submit()

        products = driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
        self.assertEqual(1, len(products))


    # def test_search_text_field(self):
    #     search_field = self.driver.find_element_by_id("search")

    
    # def test_search_text_field_by_name(self):
    #     search_field = self.driver.find_element_by_name("q")


    # def test_search_text_field_by_class_name(self):
    #     search_field = self.driver.find_element_by_class_name("input-text")


    # def test_search_button_ennabled(self): 
    #     button = self.driver.find_element_by_class_name("button")


    # def test_count_of_promo_banner_images(self):#Metodo para contar cuantas imagenes hay de promocion en el banner
    #     banner_list = self.driver.find_element_by_class_name("promos")
    #     banners = banner_list.find_elements_by_tag_name('img')
    #     self.assertEqual(3, len(banners))


    # def test_vip_promo(self):
    #     vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')


    # def test_shopping_cart(self):
    #     shopping_cart_icon = self.driver.find_element_by_css_selector("div.header-minicart span.icon")


    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main(verbosity= 2)
