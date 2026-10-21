from playwright.sync_api import Page, expect


def test_shows_products_on_main_page(page: Page):
    page.goto("/")
    expect(page.get_by_text("Combination Pliers")).to_be_visible()
