'''import sys
import os
import time
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from selenium import webdriver

from tests.test_login import test_login
from tests.test_add_to_cart import test_add_product1_to_cart
#from tests.test_add_to_cart import test_add_product2_to_cart
from tests.test_checkout import test_valid_details_checkout
from tests.test_payment_gateway import test_payment_processing
from tests.test_order_details import test_placed_order

def main():
    driver = webdriver.Chrome()
    
    test_login(driver)
        
    test_add_product1_to_cart(driver)
    #test_add_product2_to_cart(driver)

    test_valid_details_checkout(driver)

    test_payment_processing(driver)

    test_placed_order(driver)

    
if __name__ == "__main__":
    main()'''