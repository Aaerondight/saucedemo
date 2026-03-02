from playwright.sync_api import Playwright
import os
import pytest
from dotenv import load_dotenv
import allure
load_dotenv() #needs to be before importing USERS and PASSWORD

@pytest.fixture(scope="session")
def browser(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def set_up_context(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto(os.getenv("BASE_URL"))
    yield page
    context.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":  # only after test body finishes
        page = item.funcargs.get("set_up_context")
        if page:
            screenshot = page.screenshot()
            
            if rep.failed:
                allure.attach(
                    screenshot,
                    name="failure-screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
            elif rep.passed:
                allure.attach(
                    screenshot,
                    name="success-screenshot",
                    attachment_type=allure.attachment_type.PNG
                )