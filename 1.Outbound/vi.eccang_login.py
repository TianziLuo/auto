from playwright.sync_api import sync_playwright, TimeoutError
import time

USERNAME = "9518010205"
PASSWORD = "Sandy168!"

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=False)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()

    page.goto("https://home.eccang.com/login")
    page.fill('input[id="userName"]', USERNAME)
    page.fill('input[id="password"]', PASSWORD)
    page.locator('span.home-ant-checkbox').click()
    page.locator('a.ec-login-submit').click()
    
    # 等待页面加载完成
    page.wait_for_load_state("networkidle")
    print("✅ 登录成功")

    time.sleep(5)
    # 点击包含“出库单管理”的 tab 项
    tab_item = page.locator("li.entry-multi-tab-item", has_text="出库单管理")
    tab_item.wait_for(state="visible", timeout=100000)
    tab_item.click()

    # （可选）等待点击后的页面加载完成
    page.wait_for_load_state("networkidle")
    print("✅ 已点击“出库单管理”")

    # 🔄 刷新当前页面
    page.reload()
    print("🔄 页面已刷新")
    
    input("🕒 脚本暂停，按 Enter 键退出...")
