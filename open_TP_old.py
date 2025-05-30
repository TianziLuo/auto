from playwright.sync_api import sync_playwright

USERNAME = "colourtree"
EMAIL = "colourtreeusa@gmail.com"
PASSWORD = "Colourtree168!"  # Replace with your actual password

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Go to the login page
    page.goto("https://www.teapplix.com/auth/")

    # Fill in the login form (you might need to adjust selectors)
    page.fill('input[type="text"]', USERNAME)
    page.fill('input[type="email"]', EMAIL)
    page.fill('input[type="password"]', PASSWORD)

    # Click the login button (blue button with arrow icon)
    page.click('button.ant-btn-primary')

    # Wait for navigation or confirmation
    page.wait_for_load_state("networkidle")

    # Optionally, verify login success
    print("Page title after login:", page.title())

    # Keep browser open for inspection
    # browser.close()