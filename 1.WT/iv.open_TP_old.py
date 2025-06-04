from playwright.sync_api import sync_playwright
import time
import os

USERNAME = "colourtree"
EMAIL = "colourtreeusa@gmail.com"
PASSWORD = "Colourtree168!"  # Replace with your actual password

# 目标路径（注意：确保文件夹存在，否则需手动创建或用 os.makedirs）
target_folder = r"C:\Frank\原始数据\店小秘+TP+订单+盘点"
filename = "老TP订单下载 order_report.csv"
file_path = os.path.join(target_folder, filename)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=chrome_path, headless=False)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()

    # 登录
    page.goto("https://www.teapplix.com/auth/")
    page.fill('input[placeholder="账户名"]', USERNAME)
    page.fill('input[placeholder="登录电子邮件"]', EMAIL)
    page.fill('input[placeholder="密码"]', PASSWORD)

    page.click('button.ant-btn-primary')
    page.wait_for_load_state("networkidle")
    print("✅ 登录成功")

    # 进入报表
    page.wait_for_selector("text=Reports", timeout=10000)
    page.click("text=Reports")
    page.wait_for_selector("text=Order Report", timeout=10000)
    page.click("text=Order Report")
    print("✅ 已进入 Order Report 页面")

    # 勾选 shipped，取消 open
    page.locator('input.ant-checkbox-input[value="open"]').uncheck()
    page.locator('input.ant-checkbox-input[value="shipped"]').check()
    time.sleep(10)

    # 导出 CSV
    page.wait_for_selector("text=One line per order item", timeout=10000)
    page.click("text=One line per order item")

    with page.expect_download() as download_info:
        page.click("text=Export to CSV")
    download = download_info.value
    download.save_as(file_path)
    print(f"✅ 文件已保存并覆盖：{file_path}")

    input("🟢 页面已准备好，按 Enter 关闭浏览器...")
    browser.close()
