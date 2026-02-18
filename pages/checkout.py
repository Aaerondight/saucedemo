class Checkout:

    def __init__(self, page) -> None:
        self.page = page
        self.first_name = self.page.get_by_role("textbox", name="First Name")
        self.last_name = self.page.get_by_role("textbox", name="Last Name")
        self.zip = self.page.get_by_role("textbox", name="Zip")
        self.continue_button = self.page.get_by_role("button", name="Continue")
        self.overview_title = self.page.get_by_text("Checkout: Overview")
        self.finish_button = self.page.get_by_role("button", name="Finish")