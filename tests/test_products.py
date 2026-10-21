from playwright.sync_api import Page, expect

from pages import HomePage


def test_shows_products_on_main_page(page: Page):
    home_page = HomePage(page)
    home_page.goto()
    expect(page.get_by_text("Combination Pliers")).to_be_visible()
