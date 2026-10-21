from playwright.sync_api import Page, expect
from data.customer import customer
from pages import (
    BankTransferDetails,
    BillingAddress,
    CheckoutPage,
    Header,
    HomePage,
    LoginPage,
    ProductPage,
)


def test_complete_a_purchase(page: Page):
    product_name = "Bolt Cutters"
    login_page = LoginPage(page)
    home_page = HomePage(page)
    product_page = ProductPage(page)
    header = Header(page)
    checkout_page = CheckoutPage(page)

    # Step 1: log in first. The login form inside the checkout has the same
    # labels as the one in the header, so get_by_label would match two
    # elements there.
    login_page.goto()
    login_page.login(customer["email"], customer["password"])
    expect(page.get_by_role("heading", name="My account")).to_be_visible()

    # Step 2: add a product to the cart.
    home_page.goto()
    home_page.open_product(product_name)
    product_page.add_to_cart()
    expect(page.get_by_role("alert")).to_contain_text(
        "Product added to shopping cart"
    )
    expect(header.cart_link()).to_have_text("1")

    # Step 3: go to the checkout.
    header.open_cart()
    checkout_page.proceed_to_checkout()
    expect(page.get_by_text("You can proceed to checkout.")).to_be_visible()
    checkout_page.proceed_to_checkout()

    # Step 4: fill the billing address. US + 60601 on purpose: the API
    # rejects (422) a postal code whose format does not match the country.
    checkout_page.fill_billing_address(
        BillingAddress(
            country="United States of America (the)",
            postal_code="60601",
            house_number="476",
            street="Main St Test",
            city="Chicago",
            state="Illinois",
        )
    )
    checkout_page.proceed_to_checkout()
    expect(page.get_by_role("heading", name="Payment")).to_be_visible()

    # Step 5: pay and confirm the order.
    checkout_page.pay_with_bank_transfer(
        BankTransferDetails(
            bank_name="Bank of America",
            account_name="Test User",
            account_number="998877112",
        )
    )
    expect(page.locator('[data-test="payment-success-message"]')).to_be_visible()
    checkout_page.confirm()
    expect(page.get_by_text("Thanks for your order!")).to_be_visible()
