from playwright.sync_api import Page, expect
from pages.product_page import ProductPage


def test_add_a_product_to_the_cart(page: Page):
    product = ProductPage(page)
    page.goto("/")
    page.get_by_role("heading", name="Combination Pliers").click()
    expect(page.get_by_role("heading", name="Combination Pliers")).to_be_visible()
    product.add_to_cart()
    expect(page.get_by_role("alert")).to_contain_text("Product added to shopping cart")
    expect(page.get_by_role("link", name="cart")).to_have_text("1")
