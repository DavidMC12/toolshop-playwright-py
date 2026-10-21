from playwright.sync_api import Page


class ProductPage:
    def __init__(self, page: Page):
        self.page = page

    def add_to_cart(self):
        self.page.get_by_role("button", name="Add to cart").click()
