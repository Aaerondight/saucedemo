from playwright.sync_api import Playwright
import pytest
import os
from dotenv import load_dotenv
load_dotenv() #needs to be before importing USERS and PASSWORD
from pages.login import Login
from  utils.users import USERS, PASSWORD

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

@pytest.fixture(scope="function")
def standard_user(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto(os.getenv("BASE_URL"))
    login = Login(page)
    login.login(USERS["standard"], PASSWORD)
    yield page
    context.close()
