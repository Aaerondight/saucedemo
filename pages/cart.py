class Cart:

    def __init__(self, page) -> None:
        self.page = page
        self.cart = self.page.locator(".shopping_cart_link")
        self.cart_badge = self.cart.locator(".shopping_cart_badge")
        self.cart_item = self.page.locator("[data-test='inventory-item']")
        self.checkout = self.page.get_by_role("button", name="Checkout")

    def add_to_cart(self, product_name):
        product = self.page.locator("[data-test='inventory-item']", 
                                    has=self.page.get_by_text(product_name))
        product.get_by_role("button", name="Add to cart").click()
    
    def remove_from_cart(self, product_name):
        product = self.page.locator("[data-test='inventory-item']", 
                                    has=self.page.get_by_text(product_name))
        product.get_by_role("button", name="Remove").click()

    def cart_count(self):
        if self.cart_badge.is_visible():
            return int(self.cart_badge.inner_text())
        else:
            return 0
        
    def navigate_to_cart(self):
        self.cart.click()

    def checkout_cart(self):
        self.checkout.click()

    
