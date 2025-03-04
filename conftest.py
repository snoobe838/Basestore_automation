import os
import threading
import pytest
from selenium import webdriver
from pytest_html import extras 
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from utils.email_utils import send_email

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions



import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

@pytest.fixture(scope="session")
def driver(request):
    
    browser = request.config.getoption("--browser")  # Read browser option

    if browser == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)

    elif browser == "edge":
        edge_options = EdgeOptions()
        edge_options.add_argument("--start-maximized")
        driver = webdriver.Edge(options=edge_options)

    else:
        raise ValueError("Invalid browser: Choose either 'chrome' or 'edge'")

    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome or edge")



def pytest_html_report_title(report):
    report.title = "Automation Test for Happy path of BaseStore"


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # if test fails
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            try:

                screenshots_dir = os.path.join("reports", "screenshots")
                os.makedirs(screenshots_dir, exist_ok=True)

                screenshot_name = f"{item.name.replace('/', '_')}.png"
                screenshot_path = os.path.join(screenshots_dir, screenshot_name)

                driver.save_screenshot(screenshot_path)

                if hasattr(report, "extra"):
                    report.extra = report.extra or []
                    report.extra.append(extras.image(screenshot_path))

            except Exception as e:
                print(f"Error in screenshot hook: {e}")

def pytest_sessionfinish(session, exitstatus):
    send_email('reports/test_report.html') 
