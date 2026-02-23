class Overview:

    def __init__(self, page):
        self.page = page
        self.title = page.get_by_title("Checkout: Overview")
        self.item_pricee = page.locator(".inventory_item_price")
        self.total_item_price = page.locator(".summary_subtotal_label").get_by_text("Item total: $")
        self.total_price = page.locator(".summary_total_label").get_by_text("Total: $")
