from playwright.sync_api import sync_playwright
import time
import os

# Login credentials
USERNAME = "wayfaircolourtree"
EMAIL = "wayfair.colourtree@gmail.com"
PASSWORD = "Colourtree168!!"  

# Path to save the CSV file
target_folder = r"C:\Frank\原始数据\店小秘+TP+订单+盘点"
filename = "新TP订单下载 order_report.csv"
file_path = os.path.join(target_folder, filename)

# Chrome browser path
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

with sync_playwright() as p:
    # Launch browser with specified Chrome path
    browser = p.chromium.launch(executable_path=chrome_path, headless=False)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()

    # Login
    page.goto("https://www.teapplix.com/auth/")
    page.fill('input[placeholder="账户名"]', USERNAME)
    page.fill('input[placeholder="登录电子邮件"]', EMAIL)
    page.fill('input[placeholder="密码"]', PASSWORD)

    page.click('button.ant-btn-primary')
    page.wait_for_load_state("networkidle")
    print("✅ Login successful")

    # Navigate to report page
    page.wait_for_selector("text=Reports", timeout=10000)
    page.click("text=Reports")
    page.wait_for_selector("text=Order Report", timeout=10000)
    page.click("text=Order Report")

    # Select 'shipped' orders only
    page.locator('input.ant-checkbox-input[value="open"]').uncheck()
    page.locator('input.ant-checkbox-input[value="shipped"]').check()
    time.sleep(10)

    # Select output format: one line per order item
    page.wait_for_selector("text=One line per order item", timeout=10000)
    page.click("text=One line per order item")

    # Trigger download and save file
    with page.expect_download() as download_info:
        page.click("text=Export to CSV")
    download = download_info.value
    download.save_as(file_path)
    print(f"✅ File saved and overwritten: {file_path}")

    browser.close()
