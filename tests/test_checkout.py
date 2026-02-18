from playwright.sync_api import expect
from pages.cart import Cart
from pages.checkout import Checkout
from utils.helpers import set_up_cart
from utils.items import ITEMS

def test_checkout(standard_user) -> None:
    page = standard_user
    cart = Cart(page)
    checkout = Checkout(page)
    set_up_cart(page)
    cart.navigate_to_cart()

    for items in ITEMS.values():
        expect(cart.cart_item.get_by_text(items["name"])).to_be_visible()

    cart.remove_from_cart("Sauce Labs Bike Light")
    expect(cart.cart_item.get_by_text("Sauce Labs Bike Light")).not_to_be_visible()
    cart.checkout_cart()
    


