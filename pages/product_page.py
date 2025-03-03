from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage
import logging
import time

class ProductPage(BasePage):
    
    HomePageIcon = (By.XPATH, "//img[@alt='Online Store']")
    SearchIcon = (By.XPATH, "//span[@class='bsticon bst-search']")
    SearchField = (By.ID, "key")

    Product1 = (By.XPATH, "//a[text()='Sport-Tek Dry Zone Short Sleeve Raglan T-Shirt']")
    ColorSelection = (By.XPATH, "//a[contains(.,'blue')]")            
    SizeSelection = (By.CSS_SELECTOR, ".SM > i")       
    AddToCartBtn1 = (By.XPATH, "//a[contains(@class, 'btn btn-primary') and @id='js-item-addtocartbtn-165065']")
    AddToCartBtn2 = (By.XPATH, "//a[contains(@class, 'btn btn-primary') and @id='js-item-addtocartbtn-165084']")
    CartVerification = (By.XPATH, "//h3[contains(text(), 'My Cart')]")


    def open_detail_1(self, keyword):
        
        self.click(*self.SearchIcon)
        self.enter_keys(*self.SearchField, keyword)
        time.sleep(1)
        self.logger.info("Opened the detail page of the product 1")

    def open_detail_2(self):
        
        self.click(*self.HomePageIcon)
        time.sleep(3)
        self.move_to_element(*self.Product1)
        self.click(*self.Product1)
        self.logger.info("Opened the detail page of the product 2")

    def select_variation(self):
        self.logger.info("Selecting variations")
        self.click(*self.ColorSelection)

        self.click(*self.SizeSelection)

    def add_to_cart(self):
        
        self.logger.info("Adding item in cart")
        try:

            AddToCartBtn = None

            if self.is_element_present(*self.AddToCartBtn1):
                AddToCartBtn = self.AddToCartBtn1
            elif self.is_element_present(*self.AddToCartBtn2):
                AddToCartBtn = self.AddToCartBtn2

            if AddToCartBtn:
                self.move_to_element(*AddToCartBtn)
                time.sleep(1)
                self.click(*AddToCartBtn)

                self.wait_for_element_to_be_present(*self.CartVerification)
                if self.is_element_present(*self.CartVerification):
                    self.logger.info("Item added to cart.")
                else:
                    self.logger.warning("Item wasn't added to cart.")
            else:
                self.logger.error("No 'Add to Cart' button found.")
                raise Exception("No 'Add to Cart' button available.")

                
        except Exception as e:
            self.logger.error(f"Failed to add item to cart: {str(e)}")
            raise  