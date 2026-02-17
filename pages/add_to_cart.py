class AddToCart:

    def __init__(self, page) -> None:
        self.page = page
        self.cart = self.page.locator(".shopping_cart_link")
        self.count = 0

    def add_to_cart(self, product_name):
        product = self.page.locator(".inventory_item", 
                                    has=self.page.get_by_text(product_name))
        product.get_by_role("button", name="Add to cart").click()
        self.count +=1
    
    def remove_from_cart(self, product_name):
        product = self.page.locator(".inventory_item", 
                                    has=self.page.get_by_text(product_name))
        product.get_by_role("button", name="Remove").click()
        self.count -=1

    def cart_count(self):
        return self.cart.get_by_text(str(self.count))