from selenium.webdriver.common.by import By
from .base_page import BasePage
import logging
import time

class CheckoutPage(BasePage):

    CheckoutBtn = (By.ID, "checkoutbtn")
    NoBtn = (By.XPATH, "//button[text()='Not at this time']")

    Address1 = (By.ID, "addresses.billingAddress.address1")
    Country = (By.ID, "addresses.billingAddress.countryId")
    State = (By.ID, "otherregionForBilling")
    City = (By.ID, "addresses.billingAddress.city")
    Zip = (By.ID, "addresses.billingAddress.postal")


    ContinueBtn1= (By.XPATH, "//input[@type='button' and @value='Continue']")
    ContinueBtn2= (By.ID, "continueButton")
    RedirecIndicator = (By.XPATH, "//h1[contains(text(), 'You’ve been redirected from Automation_V3_DNU')]")
    
    
    def Filldetails(self, address_1, country_name, state_name, city_name, zip_code):
        
        while True:
            try:
                self.click(*self.CheckoutBtn)
                self.logger.info("Clicked on checkout button")
                time.sleep(2)
                
                if self.is_element_present(*self.NoBtn):
                    self.click(*self.NoBtn)
                    self.logger.info("Popup detected and closed")
                    time.sleep(2)

                    continue  
                
                break

            except Exception as e:
                self.logger.error(f"Error during checkout: {str(e)}")
                raise
        
        
        '''self.wait_for_element_to_be_present(*self.Address1)
        self.logger.info("Entering the necessary details")
        self.send_keys(*self.Address1, address_1)
        self.select_dropdown_by_visible_text(*self.Country, country_name)
        self.select_dropdown_by_visible_text(*self.State, state_name)
        self.send_keys(*self.City, city_name)
        self.send_keys(* self.Zip, zip_code)
        self.logger.info("Entered all details")
        time.sleep(1)'''

        self.move_to_element(*self.ContinueBtn1)
        time.sleep(1)
        self.click(*self.ContinueBtn1)
        self.logger.info("Navigating to order confirmation page")
        time.sleep(1)

        self.move_to_element(*self.ContinueBtn2)
        time.sleep(1)
        self.click(*self.ContinueBtn2)
        self.logger.info("Redirecting to payment gateway")
        time.sleep(10)

        self.wait_for_element_to_be_present(*self.RedirecIndicator)

        if self.is_element_present(*self.RedirecIndicator):
            self.logger.info("Redirected to payment gateway")
        else:
            self.logger.warning("Something went wrong")

        

