import pytest
from playwright.sync_api import expect
from pages.login import Login
from pages.cart import Cart
from pages.checkout import Checkout
from utils.helpers import set_up_cart
from utils.items import ITEMS
from utils.users import USERS, PASSWORD
from pages.checkout import Checkout
from pages.overview import Overview
from pages.checkout_complete import Complete

@pytest.mark.parametrize(
    "key",
    [
        pytest.param(k, marks=pytest.mark.xfail(strict=True))
        if k == "locked" or k == "error" or k == "problem"
        else k
        for k in USERS
    ]
)
def test_checkout(set_up_context, key) -> None:
    page = set_up_context
    login = Login(page)
    cart = Cart(page)
    checkout = Checkout(page)
    overview = Overview(page)
    complete = Complete(page)
    
    login.login(USERS[key], PASSWORD)
    expect(login.assert_variable).to_be_visible()
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

    #internal counter check
    for item in ITEMS.values():
        if item["name"] != "Sauce Labs Bike Light":
            item_price += item["price"]
    
    expect(overview.total_item_price).to_have_text("Item total: $"+str(item_price))

    #UI check
    i = 0
    item_price = 0
    while overview.item_pricee.nth(i).count() > 0:
        price = float(overview.item_pricee.nth(i).inner_text().replace("$", ""))
        #float(price)
        item_price += price
        i+=1

    expect(overview.total_item_price).to_have_text("Item total: $"+str(item_price))

    tax = float(overview.tax.inner_text().replace("Tax: $", ""))
    total_price = item_price + tax
    expect(overview.total_price).to_have_text("Total: $" + str(total_price))

    overview.click_finish()
    expect(complete.success).to_be_visible()
    
        
        

