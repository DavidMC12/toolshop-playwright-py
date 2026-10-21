from dataclasses import dataclass

from playwright.sync_api import Page


@dataclass
class BillingAddress:
    country: str
    postal_code: str
    house_number: str
    street: str
    city: str
    state: str


@dataclass
class BankTransferDetails:
    bank_name: str
    account_name: str
    account_number: str


# Cart, sign-in, billing address and payment are steps of one wizard,
# all on /checkout, so a single page object covers them.
class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    # The same button moves the wizard forward at every step.
    def proceed_to_checkout(self):
        self.page.get_by_role("button", name="Proceed to checkout").click()

    def fill_billing_address(self, address: BillingAddress):
        self.page.get_by_role("combobox", name="Country").select_option(
            label=address.country
        )
        self.page.get_by_label("Postal code").fill(address.postal_code)
        self.page.get_by_label("House number").fill(address.house_number)
        self.page.get_by_label("Street").fill(address.street)
        self.page.get_by_label("City").fill(address.city)
        self.page.get_by_label("State").fill(address.state)

    def pay_with_bank_transfer(self, details: BankTransferDetails):
        self.page.get_by_role("combobox", name="Payment Method").select_option(
            label="Bank Transfer"
        )
        self.page.get_by_label("Bank Name").fill(details.bank_name)
        self.page.get_by_label("Account Name").fill(details.account_name)
        self.page.get_by_label("Account Number").fill(details.account_number)
        self.page.get_by_role("button", name="Check payment").click()

    def confirm(self):
        self.page.get_by_role("button", name="Confirm").click()
