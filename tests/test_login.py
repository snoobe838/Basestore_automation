import sys
import os
import pytest
import time
import config  
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.login_page import LoginPage

@pytest.mark.parametrize("username, password", [
    (config.CREDENTIALS["valid_user"]["username"], config.CREDENTIALS["valid_user"]["password"]),
])

@pytest.mark.user_flow
@pytest.mark.order(1)
def test_login(driver, username, password):
    driver.get(config.BASE_URL)
    time.sleep(2)
    login_page = LoginPage(driver)
    login_page.login(username, password)
