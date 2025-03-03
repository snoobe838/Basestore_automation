from selenium.webdriver.common.by import By
from .base_page import BasePage
import logging
import time

class RegisterPage(BasePage):

    CreateNewAccountBtn = (By.ID, "create-new-account")
    FirstNameInput = (By.ID, "customerDTO.firstName")
    LastNameInput = (By.ID, "customerDTO.lastName")
    PhoneInput = (By.ID, "customerDTO.customerAddresses['1'].phone")
    CompanyInput = (By.ID, "customerDTO.customerAddresses['1'].company")
    EmailInput = (By.ID, "multilineinput")
    ConfirmEmailInput = (By.ID, "multilineinput2")
    PasswordInput = (By.ID, "customerDTO.loginpassword")
    ConfirmPasswordInput = (By.ID, "confirmPassword")

    cokkie_mess_close = (By.XPATH, "//a[@class='cookieclose ada_screen_text']")
    ContinueBtn= (By.CSS_SELECTOR, ".btn.btn-primary.continuebtn")
    RegisterSuccIndicator = (By.XPATH, "//a[@aria-label='Logout button']")
    
    def Filldetails(self, FirstName, LastName, Phone, Company,Email, ConfirmEmail, Password, ConfirmPassword):
        
        self.click(*self.cokkie_mess_close)
        self.click(*self.CreateNewAccountBtn)
        self.logger.info("Redirecting to registration page")

        self.logger.info("Entering the user info")
        self.send_keys(*self.FirstNameInput, FirstName)
        self.send_keys(*self.LastNameInput, LastName)
        self.send_keys(*self.PhoneInput, Phone)
        self.send_keys(*self.CompanyInput, Company)
        self.send_keys(*self.EmailInput, Email)
        self.send_keys(*self.ConfirmEmailInput, ConfirmEmail)
        self.send_keys(*self.PasswordInput, Password)
        self.send_keys(*self.ConfirmPasswordInput, ConfirmPassword)
        self.logger.info("Entered all details")

        self.click(*self.ContinueBtn)
        self.logger.info("clicked on Continue button")

        time.sleep(3)

        if self.is_element_present(*self.RegisterSuccIndicator):
            self.logger.info("Registration successful.")
        else:
            self.logger.warning("Registration failed.")
        

