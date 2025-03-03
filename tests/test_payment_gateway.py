import sys
import os
import pytest
import config  
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.payment_gateway_page import PaymentPage

@pytest.mark.parametrize("card_holder, card_number, cvv, exp_month, exp_year", [
    (
        config.PAYMENT_DETAILS["valid_payment"]["card_holder"],
        config.PAYMENT_DETAILS["valid_payment"]["card_number"],
        config.PAYMENT_DETAILS["valid_payment"]["cvv"],
        config.PAYMENT_DETAILS["valid_payment"]["exp_month"],
        config.PAYMENT_DETAILS["valid_payment"]["exp_year"]
    )
])

@pytest.mark.user_flow
@pytest.mark.order(4)
def test_payment_processing(driver, card_holder, card_number, cvv, exp_month, exp_year):
    payment_page = PaymentPage(driver)
    payment_page.enter_card_details(card_holder, card_number, cvv, exp_month, exp_year)
    payment_page.place_order()
    
    assert payment_page.is_element_present(*payment_page.PaymentConfIndicator), \
        "Payment should succeed. User should be redirected to order confirmation page with place order button."
