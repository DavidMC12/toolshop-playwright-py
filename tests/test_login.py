from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from data.customer import customer


def test_login_with_a_valid_user(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login(customer["email"], customer["password"])
    expect(page.get_by_role("heading", name="My account")).to_be_visible()


def test_login_with_unknown_credentials(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("non-exist@mail.com", "welcome99")
    expect(page.get_by_text("Invalid email or password")).to_be_visible()
