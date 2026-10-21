from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("/")

    def open_product(self, name: str):
        self.page.get_by_role("heading", name=name).click()
