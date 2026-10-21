from playwright.sync_api import Page, expect
from pages.header import Header
from pages.home_page import HomePage
from pages.product_page import ProductPage


def test_add_a_product_to_the_cart(page: Page):
    product_name = "Bolt Cutters"
    home_page = HomePage(page)
    product_page = ProductPage(page)
    header = Header(page)

    home_page.goto()
    home_page.open_product(product_name)
    expect(page.get_by_role("heading", name=product_name)).to_be_visible()
    product_page.add_to_cart()
    # The toast is a role="alert"; to_contain_text ignores the rest of its text.
    expect(page.get_by_role("alert")).to_contain_text(
        "Product added to shopping cart"
    )
    expect(header.cart_link()).to_have_text("1")
