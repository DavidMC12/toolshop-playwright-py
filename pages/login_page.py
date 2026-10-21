from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("/auth/login")

    def login(self, email: str, password: str):
        self.page.get_by_label("Email address *").fill(email)
        self.page.get_by_label("Password *").fill(password)
        self.page.get_by_role("button", name="Login").click()
