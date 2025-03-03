
BASE_URL = "https://qa.mypromomall.com/preview/signin.html?vid=20240130374&mt=1&redirecturl=automation1234%3Ftpt%3Ddesktop2_en&loginway=header"  

CREDENTIALS = {
    "valid_user": {"username": "snoobetest@gmail.com", "password": "Snoobe@838"},
    "invalid_user": {"username": "invalid@gmail.com", "password": "password123"},
}

PAYMENT_DETAILS = {
    "valid_payment": {
        "card_holder": "snoobe test",
        "card_number": "4111111111111111",
        "cvv": "998",
        "exp_month": "FEB",
        "exp_year": "2030"
    }
}