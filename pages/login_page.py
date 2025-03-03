from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import logging
import time

class LoginPage(BasePage):

    UsernameInput = (By.ID, "multilineinput")
    PasswordInput = (By.ID, "password")
    LoginBtn = (By.CSS_SELECTOR, ".btn.btn-primary.w-100")

    LoginSuccIndicator = (By.XPATH, "//a[@aria-label='Logout button']")
    LoginFailedIndicator = (By.XPATH, "//div[text()='The login with that password doesn't exist.']")
    cokkie_mess_close = (By.XPATH, "//a[@class='cookieclose ada_screen_text']")

    
    def login(self, username, password):

        if self.is_element_present(*self.cokkie_mess_close):
            self.click(*self.cokkie_mess_close)

        self.send_keys(*self.UsernameInput, username)
        self.send_keys(*self.PasswordInput, password)
        self.logger.info("Entered credentials")

        self.click(*self.LoginBtn)
        self.logger.info("atempting to login")
        time.sleep(3)

        if self.is_element_present(*self.LoginSuccIndicator):
            self.logger.info("Login successful.")
        else:
            self.logger.warning("Login failed.")
