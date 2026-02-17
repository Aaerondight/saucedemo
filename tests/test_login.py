from playwright.sync_api import expect
import pytest
from  utils.users import USERS, VALID_USERS, INVALID_USERS, PASSWORD
from pages.login import Login

@pytest.mark.parametrize("user_key", VALID_USERS)
def test_valid_users(set_up_context, user_key) -> None:
    page = set_up_context
    login = Login(page)
    login.login(USERS[user_key], PASSWORD)
    expect(login.assert_variable).to_be_visible()

@pytest.mark.parametrize("user_key", INVALID_USERS)
def test_locked_user(set_up_context, user_key) -> None:
    page = set_up_context
    login = Login(page)
    login.login(USERS[user_key], PASSWORD)
    expect(login.assert_variable).to_be_visible()

@pytest.mark.parametrize("username, password", [
    ("random_username", "notcorrect@123"), (USERS["standard"], "notcorrect@123"),
    ("random_username", PASSWORD)])
def test_invalid_scenarios(set_up_context, username, password) -> None:
    page = set_up_context
    login = Login(page)
    login.login(username, password)
    expect(login.invalid_msg).to_be_visible()