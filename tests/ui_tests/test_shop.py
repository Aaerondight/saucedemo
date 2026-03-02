from pages.login import Login
from utils.users import USERS, PASSWORD
from pages.cart import Cart

def test_shop_page_ui(set_up_context, assert_snapshot):
    page = set_up_context
    login = Login(page)
    cart = Cart(page)
    login.login(USERS["standard"], PASSWORD)
    assert_snapshot(page.screenshot(full_page=True, mask=[login.assert_variable]))

