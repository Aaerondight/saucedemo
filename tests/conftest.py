from playwright.sync_api import Playwright
from dotenv import load_dotenv
import pytest
import os

# Load .env file at the start
load_dotenv()

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

