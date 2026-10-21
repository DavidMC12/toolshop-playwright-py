from playwright.sync_api import Page, expect
from pages import LoginPage
from data.customer import customer


def test_login_with_a_valid_user(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login(customer["email"], customer["password"])
    # By role: the text "My account" also appears in the menu (strict mode violation).
    expect(page.get_by_role("heading", name="My account")).to_be_visible()


def test_login_with_unknown_credentials(page: Page):
    login = LoginPage(page)
    login.goto()
    # Unknown email on purpose: failing logins on a real demo user lock it.
    login.login("non-exist@mail.com", "welcome99")
    # The error box is a plain div with no role, so it is matched by text.
    expect(page.get_by_text("Invalid email or password")).to_be_visible()
