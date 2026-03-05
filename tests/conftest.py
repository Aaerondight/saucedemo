from playwright.sync_api import Playwright
import os
import pytest
from dotenv import load_dotenv
#import allure
from pathlib import Path
from datetime import datetime
from pytest_html import extras
load_dotenv() #needs to be before importing USERS and PASSWORD

@pytest.fixture(scope="session")
def browser(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def set_up_context(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto(os.getenv("BASE_URL"))
    yield page
    context.close()

#manage report path
def pytest_configure(config):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"reports/report_{timestamp}.html"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":

        page = item.funcargs["set_up_context"]

        screenshots_dir = Path("screenshots")
        screenshots_dir.mkdir(exist_ok=True)

        file_path = screenshots_dir / f"{item.name}.png"
        page.screenshot(path=str(file_path), full_page=True)

        extras_list = getattr(report, "extras", [])
        extras_list.append(extras.image(f"../{file_path}"))
        report.extras = extras_list