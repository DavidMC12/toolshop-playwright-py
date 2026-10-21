# Toolshop Playwright PY

End-to-end tests written with [Playwright](https://playwright.dev/python/) and [pytest](https://docs.pytest.org) (Python) for [Practice Software Testing](https://practicesoftwaretesting.com), a demo web shop built for testing practice.

This is a personal practice project. It is not affiliated with or endorsed by the owners of Practice Software Testing. A TypeScript version of the same suite lives in [toolshop-playwright-ts](https://github.com/DavidMC12/toolshop-playwright-ts).

## What is covered

- **Products:** the home page lists products.
- **Login:** a valid user reaches "My account"; unknown credentials show an error.
- **Cart:** a product can be added and the cart counter updates.

The tests run on Chromium by default. Firefox and WebKit are available with `--browser`.

## How it is organized

```
data/customer.py   demo user, defined once
pages/             page objects, one class per page (LoginPage, ProductPage)
tests/             tests: products, login, cart
pytest.ini         base URL and default browser
```

- **Page Object Model:** locators and actions live in `pages/`, and the tests only describe the scenario and make the assertions.
- **Locators:** role- and label-based (`get_by_role`, `get_by_label`) before anything else.
- **pytest-playwright:** the `page` fixture gives every test a fresh browser context. `expect(...)` assertions retry until they pass or time out.

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
pytest                           # all tests, headless, Chromium
pytest --headed                  # with a visible browser
pytest --headed --slowmo 700     # visible and slower
pytest --browser firefox         # another browser
pytest --browser chromium --browser firefox
pytest -k login                  # tests whose name contains "login"
pytest tests/test_cart.py        # one file
pytest --tracing on              # record a trace for each test
```

Open a recorded trace with `playwright show-trace test-results/<test-folder>/trace.zip`.

## Things worth knowing

- The tests run against the public demo site, so they depend on its availability.
- The login uses the demo user `customer2@practicesoftwaretesting.com` from the app's own README. The user `customer@practicesoftwaretesting.com` gets locked (HTTP 423) after a few failed logins, so the failed-login test uses an email that does not exist.
- There is no CI workflow. The demo site sits behind Cloudflare, which blocks GitHub-hosted runners with a bot check, so runs on every push always failed in the TypeScript project.

## License

[MIT](LICENSE)
