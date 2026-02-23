class Checkout:

    def __init__(self, page) -> None:
        self.page = page
        self.first_name = self.page.get_by_role("textbox", name="First Name")
        self.last_name = self.page.get_by_role("textbox", name="Last Name")
        self.zip = self.page.get_by_role("textbox", name="Zip")
        self.continue_button = self.page.get_by_role("button", name="Continue")
        self.overview_title = self.page.get_by_text("Checkout: Overview")
        self.finish_button = self.page.get_by_role("button", name="Finish")

    def fill_first_name(self, name):
        self.first_name.fill(name)
    
    def fill_last_name(self, name):
        self.last_name.fill(name)

    def fill_zip(self, name):
        self.zip.fill(name)

    def click_continue(self):
        self.continue_button.click()