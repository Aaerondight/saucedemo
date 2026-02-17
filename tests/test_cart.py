from playwright.sync_api import expect
from pages.add_to_cart import AddToCart

def test_cart(standard_user) -> None:
    page = standard_user
    cart = AddToCart(page)
    cart.add_to_cart("Test.allTheThings() T-Shirt (Red)")
    cart.add_to_cart("Sauce Labs Onesie")
    cart.add_to_cart("Sauce Labs Fleece Jacket")
    cart.add_to_cart("Sauce Labs Backpack")
    cart.add_to_cart("Sauce Labs Bike Light")
    cart.remove_from_cart("Test.allTheThings() T-Shirt (Red)")
    expect(cart.cart_count()).to_be_visible()

