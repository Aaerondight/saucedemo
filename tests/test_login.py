from playwright.sync_api import expect
from dotenv import load_dotenv
import os, pytest
from pages.login import Login
from utils.helpers import invalid_password, invalid_username

load_dotenv()

def test_standard_user(set_up_context) -> None:
    page = set_up_context
    login = Login(page)
    login.user_field.fill(os.getenv("STANDARD_USER"))
    login.password_field.fill(os.getenv("PASSWORD"))
    login.submit()
    expect(page.get_by_text("Products")).to_be_visible()

def test_locked_user(set_up_context) -> None:
    page = set_up_context
    login = Login(page)
    login.user_field.fill(os.getenv("LOCKED_OUT_USER"))
    login.password_field.fill(os.getenv("PASSWORD"))
    login.submit()
    expect(login.locked_msg).to_be_visible()

def test_problem_user(set_up_context) -> None:
    page = set_up_context
    login = Login(page)
    login.user_field.fill(os.getenv("PROBLEM_USER"))
    login.password_field.fill(os.getenv("PASSWORD"))
    login.submit()
    expect(page.get_by_text("Products")).to_be_visible()

def test_performance_glitch_user(set_up_context) -> None:
    page = set_up_context
    login = Login(page)
    login.user_field.fill(os.getenv("PERFORMANCE_GLITCH_USER"))
    login.password_field.fill(os.getenv("PASSWORD"))
    login.submit()
    expect(page.get_by_text("Products")).to_be_visible()

def test_error_user(set_up_context) -> None:
    page = set_up_context
    login = Login(page)
    login.user_field.fill(os.getenv("ERROR_USER"))
    login.password_field.fill(os.getenv("PASSWORD"))
    login.submit()
    expect(page.get_by_text("Products")).to_be_visible()

def test_visual_user(set_up_context) -> None:
    page = set_up_context
    login = Login(page)
    login.user_field.fill(os.getenv("VISUAL_USER"))
    login.password_field.fill(os.getenv("PASSWORD"))
    login.submit()
    expect(page.get_by_text("Products")).to_be_visible()

@pytest.mark.parametrize("username, password", [
    ("random_username", "notcorrect@123"), (os.getenv("STANDARD_USER"), "notcorrect@123"),
    ("random_username", os.getenv("PASSWORD"))])
def test_invalid_scenarios(set_up_context, username, password) -> None:
    page = set_up_context
    login = Login(page)
    login.user_field.fill(username)
    login.password_field.fill(password)
    login.submit()
    expect(login.invalid_msg).to_be_visible()