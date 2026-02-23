from playwright.sync_api import expect
from pages.cart import Cart
from pages.checkout import Checkout
from utils.helpers import set_up_cart
from utils.items import ITEMS
from pages.checkout import Checkout
from pages.overview import Overview

def test_checkout(standard_user) -> None:
    page = standard_user
    cart = Cart(page)
    checkout = Checkout(page)
    overview = Overview(page)

    set_up_cart(page)
    cart.navigate_to_cart()

    for items in ITEMS.values():
        expect(cart.cart_item.get_by_text(items["name"])).to_be_visible()

    cart.remove_from_cart("Sauce Labs Bike Light")
    expect(cart.cart_item.get_by_text("Sauce Labs Bike Light")).not_to_be_visible()
    cart.checkout_cart()

    checkout.fill_first_name("Sam")
    checkout.fill_last_name("Wise")
    checkout.fill_zip("3000")
    checkout.click_continue()

    item_price = 0

    for item in ITEMS.values():
        if item["name"] != "Sauce Labs Bike Light":
            item_price += item["price"]
    
    expect(overview.total_item_price).to_have_text("Item total: $"+str(item_price))

    i = 0
    item_price = 0
    while overview.item_pricee.nth(i).count() > 0:
        price = float(overview.item_pricee.nth(i).inner_text().replace("$", ""))
        #float(price)
        item_price += price
        i+=1

    expect(overview.total_item_price).to_have_text("Item total: $"+str(item_price))
    
        
        

