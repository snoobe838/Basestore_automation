from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from utils.logger_config import setup_logger
import pandas as pd
import pytest
import logging

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = setup_logger(self.__class__.__name__)


    def find_element(self, by, locator):
        return self.driver.find_element(by, locator)

    def click(self, by, locator):
        self.find_element(by, locator).click()

    def send_keys(self, by, locator, text):
        self.find_element(by, locator).send_keys(text)

    def enter_keys(self, by, locator, text):
        element = self.find_element(by, locator).send_keys(text + Keys.ENTER)

    def send_keys_using_prev_loc(self, by, locator, text):
        element = self.find_element(by, locator).send_keys(Keys.TAB, Keys.TAB+ text)
    
    def select_dropdown_by_visible_text(self, locator_type, locator_value, text):
        dropdown = Select(self.find_element(locator_type, locator_value))
        dropdown.select_by_visible_text(text)


    def wait_for_element_to_be_removed(self, by, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located((by, locator))
        )

    def wait_for_element_to_be_clickable(self, by, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, locator))
        )
    
    def wait_for_element_to_be_present(self, by, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, locator))
        )
    
    def wait_for_element_to_be_visible(self, by, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, locator))
        )
    
    def wait_for_text_to_be_present_in_element(self, by, locator, text, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((by, locator, text))
        )
    
    def is_element_present(self, by, value):
        try:
            element = self.driver.find_element(by, value)
            return element.is_displayed()  
        except NoSuchElementException:
            return False


    def scroll_to_element(self, by, locator):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", locator)
        
    def move_to_element(self, by, value):
        element = self.find_element(by, value)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def switch_to_iframe(self):
        self.driver.switch_to.frame(0)
        self.driver.switch_to.frame(0)

    def switch_to_main_content(self):
        self.driver.switch_to.default_content()
        self.driver.switch_to.default_content()

    def is_user_logged_in(self):
        try:
            return self.driver.find_element("xpath", "//a[contains(text(), 'Logout')]").is_displayed()
        except:
            return False

    def check_and_login(self, driver):
        if not self.is_user_logged_in():
            pytest.main(["-q", "tests/test_login.py"]) 
    
        