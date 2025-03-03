from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import logging
import time


class PaymentPage(BasePage):

    NameInput = (By.ID, "name")
    CvvInput = (By.ID, "cvv-no")
    ExpMonthInput = (By.CSS_SELECTOR, "select#month")
    ExpYearInput = (By.CSS_SELECTOR, "select#year")
    CardNumberInput = (By.ID, "ccnumfield")

    Loading_icon = (By.XPATH, "//img[@src='snappay/assets/img/cc_loader.gif' and @alt='Loading...']")
    ContinueBtn = (By.CSS_SELECTOR, "input[value='Continue']:first-of-type")
    CaptchaVerBtn = (By.CSS_SELECTOR, ".ui-dialog-buttonpane .ui-button")
    Captchafailind = (By.XPATH, "//button[@class='ui-dialog-titlebar-close']")

    PaymentConfIndicator = (By.ID, "placeord")
    ContinueBtn2= (By.ID, "continueButton")
    
    
    def enter_card_details(self, card_holder, card_number, cvv, exp_month, exp_year):

        self.wait_for_element_to_be_removed(*self.Loading_icon,60)

        time.sleep(3)
        self.send_keys(*self.NameInput, card_holder)
        self.logger.info("Entered Card holder name")
        time.sleep(1)

        self.switch_to_iframe()
        self.logger.info("Switched to iframe")
        time.sleep(2)

        self.move_to_element(*self.CardNumberInput)
        time.sleep(2)
        self.click(*self.CardNumberInput)
        self.send_keys(*self.CardNumberInput, card_number)
        self.logger.info("Entered card number")
        time.sleep(2)

        self.switch_to_main_content()
        self.logger.info("Switched back to main")
        time.sleep(1)

        self.select_dropdown_by_visible_text(*self.ExpMonthInput, exp_month)
        self.select_dropdown_by_visible_text(*self.ExpYearInput, exp_year)
        self.logger.info("Entered card Exp date")

        time.sleep(1)
        self.send_keys(*self.CvvInput, cvv)
        self.logger.info("Entered cvv number")

        time.sleep(3)
        self.logger.info("Entered Payment details")
        

        while True:
            try:
                self.move_to_element(*self.ContinueBtn)
                time.sleep(2)
                self.click(*self.ContinueBtn)
                self.logger.info("Checking if captcha required...")
                time.sleep(10)
                
                if self.is_element_present(*self.CaptchaVerBtn):
                    self.move_to_element(*self.CaptchaVerBtn)
                    self.logger.info("Captcha button found.")
                    time.sleep(2)
                    self.click(*self.CaptchaVerBtn)
                    self.logger.info("Clicking Captcha button.")
                    time.sleep(3)

                    if self.is_element_present(*self.Captchafailind):
                        self.move_to_element(*self.Captchafailind)
                        self.click(*self.Captchafailind)
                        self.logger.warning("Payment unsuccessful due to multiple failed captcha attempts.")
                        return  # Stop execution

                    continue  
                
                break

            except Exception as e:
                self.logger.error(f"Error during processing: {str(e)}")
                raise

        self.wait_for_element_to_be_present(*self.PaymentConfIndicator)

    def place_order(self):
        if self.is_element_present(*self.PaymentConfIndicator):
            self.logger.info("Payment Successful.")
        else:
            self.logger.error("Payment failed.")

        