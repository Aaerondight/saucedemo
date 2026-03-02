class Complete:

    def __init__(self, page):
        self.page = page
        self.success = page.get_by_text("Thank you for your order!")
        self.home_button = page.get_by_role("button", name="Back home")
