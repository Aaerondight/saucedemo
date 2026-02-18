from pages.cart import Cart
from utils.items import ITEMS

def set_up_cart(page) -> None:
    cart = Cart(page)

    for item in ITEMS.values():
        cart.add_to_cart(item["name"])
       

