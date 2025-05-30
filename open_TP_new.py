from playwright.sync_api import sync_playwright
import time
import os

download_dir = "C:\\Frank\\Downloads\\Teapplix"

context = browser.new_context(accept_downloads=True, downloads_path=download_dir)
USERNAME = "wayfaircolourtree"
EMAIL = "wayfair.colourtree@gmail.com"
PASSWORD = "Colourtree168!!"  # Replace with your actual password

# 修改为你本地 Chrome 的路径（根据实际安装位置）
chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=chrome_path, headless=False)
    context = browser.new_context(accept_downloads=True, downloads_path="C:\\Downloads")
    page = context.new_page()

    # 登录
    page.goto("https://www.teapplix.com/auth/")
    page.fill('input[type="text"]', USERNAME)
    page.fill('input[type="email"]', EMAIL)
    page.fill('input[type="password"]', PASSWORD)
    page.click('button.ant-btn-primary')
    page.wait_for_load_state("networkidle")
    print("✅ 登录成功")

    # Step 2: 进入 Order Report 页面
    page.wait_for_selector("text=Reports", timeout=10000)
    page.click("text=Reports")
    page.wait_for_selector("text=Order Report", timeout=10000)
    page.click("text=Order Report")
    print("✅ 已进入 Order Report 页面")

    # Step 3: 勾选 shipped，取消 open
    page.locator('input.ant-checkbox-input[value="open"]').uncheck()
    page.locator('input.ant-checkbox-input[value="shipped"]').check()
    time.sleep(10)

    # Step 4: 选择时间选项并导出
    page.wait_for_selector("text=One line per order item", timeout=10000)
    page.click("text=One line per order item")

    page.wait_for_selector("text=Export to CSV", timeout=10000)
    page.click("text=Export to CSV")

    input("🟢 页面已准备好，按 Enter 关闭浏览器...")
    browser.close()
