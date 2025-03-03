import time
import pytest
from selenium import webdriver
from pages.product_page import ProductPage

@pytest.mark.user_flow
@pytest.mark.order(2)
def test_add_product1_to_cart(driver):
    product_page = ProductPage(driver)
    driver.get("https://qa.mypromomall.com/preview/automation1234")
    time.sleep(3)

    product_page.open_detail_1("pen")
    time.sleep(2)
    product_page.add_to_cart()

def test_add_product2_to_cart(driver):
    product_page = ProductPage(driver)
    driver.get("https://qa.mypromomall.com/preview/automation1234")
    time.sleep(2)
    product_page.open_detail_2()
    time.sleep(2)
    product_page.select_variation()
    product_page.add_to_cart()


