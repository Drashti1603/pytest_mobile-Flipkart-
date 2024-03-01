import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import Mobile_Locators
from Config.config import my_input, my_num

class Main:
    def __init__(self, driver):
        self.driver = driver
    
    def capture_screenshot(self, filename):
        self.driver.save_screenshot(os.path.join(os.getcwd(), "Tests", "Mobile", "Results", filename + ".png"))

###---SEARCH---###
class SearchPage(Main):
    def test_searching(self): 
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, Mobile_Locators.skip))).click()
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, Mobile_Locators.categories))).click()
            WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, Mobile_Locators.SearchButton))).click()
            search_query = my_input() 
            search_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Mobile_Locators.SearchFieldLocator)))
            search_field.click()
            search_field.send_keys(search_query)
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Mobile_Locators.SearchButton1))).click()
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, Mobile_Locators.allow))).click()
        except Exception as e:
            self.capture_screenshot("searching_failed")
            print(e)

###---FILTER---###
class FilterPage(Main):

    def test_filter(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Mobile_Locators.brand))).click()
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Mobile_Locators.adidas))).click()
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Mobile_Locators.apply))).click()
        except Exception as e:
            self.capture_screenshot("filter_failed")
            print(e)
        
###---SELECT---###
class SelectPage(Main):
   
    def test_selecting(self):
        try:
            # prod1 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Mobile_Locators.Product1)))
            # prod2 = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, Mobile_Locators.Product6)))
            # self.driver.scroll(prod1, prod2)
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Mobile_Locators.prod))).click()
            WebDriverWait(self.driver, 10)
            
        except Exception as e:
            self.capture_screenshot("select_failed")
            print(e)

###---CART---###
class CartPage(Main):

    def test_cart_and_login(self):
        try:
            try:
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Mobile_Locators.add_to_cart1))).click()
            except:
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Mobile_Locators.add_to_cart))).click()

            try:
                search_query = my_num() 
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, f'//android.widget.TextView[@text= "{search_query}"]'))).click()
                try:
                    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Mobile_Locators.conti))).click()
                except:    
                    print("Not Available Try Other")
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Mobile_Locators.go_to_cart))).click()
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Mobile_Locators.remove_item))).click()
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Mobile_Locators.remove))).click()
            except:
                print("Not Correct. Rerun and enter correct size!!!!")
                self.capture_screenshot("cart_failed")

        
        except Exception as e:
            self.capture_screenshot("cart_failed")
            print(e)        

###FAILED###
class Login(Main):
    def login(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Mobile_Locators.Phn_input))).click()
            self.driver.save_screenshot(os.path.join(os.getcwd(), "Tests", "Mobile", "Results",  "nopage.png"))

        except:
            self.driver.save_screenshot(os.path.join(os.getcwd(), "Tests", "Mobile", "Results",  "nopage.png"))
                  

