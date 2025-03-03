import sys
import os
import pytest
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from selenium import webdriver
from pages.checkout_page import CheckoutPage
from utils.data_utils import read_test_data


'''with open("test_data.json") as file:
    test_data = json.load(file)

@pytest.mark.parametrize(
    "address_1, country_name, state_name, city_name, zip_code",
    [
        (
            test_data["address_details"]["valid_checkout"]["address_1"],
            test_data["address_details"]["valid_checkout"]["country_name"],
            test_data["address_details"]["valid_checkout"]["state_name"],
            test_data["address_details"]["valid_checkout"]["city_name"],
            test_data["address_details"]["valid_checkout"]["zip_code"]
        )
    ]
)'''

@pytest.mark.parametrize("address_1, country_name, state_name, city_name, zip_code", 
    read_test_data("test_data.xlsx", "address_details")
)

@pytest.mark.user_flow
@pytest.mark.order(3)
def test_valid_details_checkout(driver, address_1, country_name, state_name, city_name, zip_code):
    checkout_page = CheckoutPage(driver)
    checkout_page.Filldetails(address_1, country_name, state_name, city_name, zip_code)

