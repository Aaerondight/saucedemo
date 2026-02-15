from playwright.sync_api import Playwright
import pytest

@pytest.fixture(scope="function")
def browser(playwright: Playwright):
    browser = playwright.chromium.launch()
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def set_up_context(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    yield page
    context.close()

