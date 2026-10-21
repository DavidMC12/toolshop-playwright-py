from playwright.sync_api import Locator, Page


# Navigation bar, present on every page.
class Header:
    def __init__(self, page: Page):
        self.page = page

    # Returns the locator so tests can assert on it, e.g. the item count.
    def cart_link(self) -> Locator:
        return self.page.get_by_role("link", name="cart")

    def open_cart(self):
        self.cart_link().click()
