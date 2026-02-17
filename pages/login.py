class Login:

    def __init__(self, page):
        self.page = page 
        self.user_field = page.get_by_role("textbox", name="Username")
        self.password_field = page.get_by_role("textbox", name="Password")
        self.submit_button = page.get_by_role("button", name="Login")
        self.locked_msg = page.get_by_text("Epic sadface: Sorry, this user has been locked out.")
        self.invalid_msg = page.get_by_text("Epic sadface: Username and password do not match any user in this service")
        self.assert_variable = page.get_by_text("Products")
        
    def login(self, username, password):
        self.user_field.fill(username)
        self.password_field.fill(password)
        self.submit_button.click()
