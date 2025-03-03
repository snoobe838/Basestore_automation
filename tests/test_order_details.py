import time
import pytest
from selenium import webdriver
from pages.order_details_page import OrderConf

@pytest.mark.user_flow
@pytest.mark.order(5)
def test_placed_order(driver):
    order_detail_page = OrderConf(driver)
    time.sleep(3)

    order_detail_page.Order_details()
