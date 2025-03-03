from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import logging
import time


class OrderConf(BasePage):

    PlaceOrderBtn = (By.ID, "placeord")
    ConfirmationMessage = (By.XPATH, "//div[text()='Thank you for your order!']")
    OrderId_element = (By.XPATH, "//div[contains(text(), 'Order Confirmation Number:')]/strong")
    LoginBtn = (By.CSS_SELECTOR, ".btn.btn-primary.w-100")
    
    

    
    def Order_details(self):

        self.click(*self.PlaceOrderBtn)
        time.sleep(3)
        OrderId = self.find_element(*self.OrderId_element).text
        self.logger.info(f"Order is placed. Order ID: {str(OrderId)}")

    
