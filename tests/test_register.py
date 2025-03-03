import sys
import os
import pytest
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from selenium import webdriver
from pages.register_page import RegisterPage
from utils.data_utils import read_test_data
import config

'''with open("test_data.json") as file:
    test_data = json.load(file)

@pytest.mark.parametrize(
    "FirstName, LastName, Phone, Company, Email, ConfirmEmail, Password, ConfirmPassword, expected_result", [
        (
            test_data["register_details"]["valid_register"]["FirstName"],
            test_data["register_details"]["valid_register"]["LastName"],
            test_data["register_details"]["valid_register"]["Phone"],
            test_data["register_details"]["valid_register"]["Company"],
            test_data["register_details"]["valid_register"]["Email"],
            test_data["register_details"]["valid_register"]["ConfirmEmail"],
            test_data["register_details"]["valid_register"]["Password"],
            test_data["register_details"]["valid_register"]["ConfirmPassword"],
            True
        )
    ]
)'''

@pytest.mark.parametrize("FirstName, LastName, Phone, Company, Email, ConfirmEmail, Password, ConfirmPassword", 
    read_test_data("test_data.xlsx", "register_details")
)


def test_valid_registration(driver, FirstName, LastName, Phone, Company, Email, ConfirmEmail, Password, ConfirmPassword):
    
    driver.get(config.BASE_URL)

    register_page = RegisterPage(driver)
    register_page.Filldetails(FirstName, LastName, Phone, Company, Email, ConfirmEmail, Password, ConfirmPassword)


    assert register_page.is_element_present(*register_page.RegisterSuccIndicator), "User should be registered and logged in."