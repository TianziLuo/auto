from playwright.sync_api import sync_playwright
from playwright.sync_api import sync_playwright, expect
import time

USERNAME = "annie515"
PASSWORD = "Annie1688!"  

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=chrome_path, headless=False)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()

    # login
    page.goto("https://www.dianxiaomi.com/index.htm?ts=1748650137")
    page.fill('input[placeholder="请输入用户名"]', USERNAME)
    page.fill('input[placeholder="请输入密码"]', PASSWORD)

    # CODE
    time.sleep(10)

    page.get_by_text("登录", exact=True).click()
    page.wait_for_selector('text=登录', timeout=10000)
    print("✅ 登录成功")
