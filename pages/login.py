class Login:

    def __init__(self, page):
        self.page = page 
        self.user_field = page.get_by_role("textbox", name="Username")
        self.password_field = page.get_by_role("textbox", name="Password")
        self.submit_button = page.get_by_role("button", name="Login")
        self.locked_msg = page.get_by_text("Epic sadface: Sorry, this user has been locked out.")
        self.invalid_msg = page.get_by_text("Epic sadface: Username and password do not match any user in this service")

    def submit(self):
        self.submit_button.click()
