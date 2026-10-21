# Toolshop Playwright PY

End-to-end tests written with [Playwright](https://playwright.dev/python/) and [pytest](https://docs.pytest.org) (Python) for [Practice Software Testing](https://practicesoftwaretesting.com), a demo web shop built for testing practice.

This is a personal practice project. It is not affiliated with or endorsed by the owners of Practice Software Testing. The same suite, written in TypeScript, lives in [toolshop-playwright-ts](https://github.com/DavidMC12/toolshop-playwright-ts).

## What is covered

- **Products:** the home page lists products.
- **Login:** a valid user reaches "My account"; unknown credentials show an error.
- **Cart:** a product can be added and the cart counter updates.
- **Checkout:** a full purchase, from login to the order confirmation.

The tests run on Chromium and Firefox.

## How it is organized

```
data/customer.py   demo user, defined once
pages/             page objects, one class per page or shared component
                   (HomePage, ProductPage, LoginPage, CheckoutPage, Header)
tests/             tests: products, login, cart, checkout
pytest.ini         base URL, browsers, trace on failure
ruff.toml          formatter and linter settings
```

- **Page Object Model:** locators and actions live in `pages/`, and the tests only describe the scenario and make the assertions. `pages/__init__.py` exports every page object, so a test imports them with `from pages import LoginPage`.
- **Locators:** role- and label-based (`get_by_role`, `get_by_label`) before anything else.
- **pytest-playwright:** the `page` fixture gives every test a fresh browser context. `expect(...)` assertions retry until they pass or time out.
- **Data objects:** the checkout takes `BillingAddress` and `BankTransferDetails` dataclasses instead of a long list of strings.

## Getting started

You need Python 3.

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium firefox
```

On Debian or Ubuntu, `playwright install --with-deps` also installs the system libraries.

## Running the tests

```bash
pytest                           # all tests, headless, Chromium and Firefox
pytest --headed                  # with a visible browser
pytest --headed --slowmo 700     # visible and slower
pytest -k chromium               # only one browser (-k firefox for the other)
pytest -k login                  # tests whose name contains "login"
pytest tests/test_cart.py        # one file
pytest -x                        # stop at the first failure
```

A trace is recorded for every failed test. Open it with `playwright show-trace test-results/<test-folder>/trace.zip`.

## Formatting and linting

The code is formatted and checked with [Ruff](https://docs.astral.sh/ruff/). The settings are in `ruff.toml`.

```bash
pip install -r requirements-dev.txt
ruff format .                    # format the code
ruff check .                     # lint (add --fix to apply the safe fixes)
```

## Things worth knowing

- The browsers are set in `pytest.ini`. Do not add `--browser` on the command line: it is added to the ones in the file and runs them twice. Use `-k chromium` or `-k firefox` to pick one.
- The tests run against the public demo site, so they depend on its availability.
- The login uses the demo user `customer2@practicesoftwaretesting.com` from the app's own README. The user `customer@practicesoftwaretesting.com` gets locked (HTTP 423) after a few failed logins, so the failed-login test uses an email that does not exist.
- The checkout uses a US address with postal code `60601` on purpose: the API rejects a postal code that does not match the country.
- The GitHub Actions workflow is manual (`workflow_dispatch`). The demo site sits behind Cloudflare, which blocks GitHub-hosted runners with a bot check, so runs on every push always failed in the TypeScript project. The Python workflow has not been run for the same reason.

## License

[MIT](LICENSE)
