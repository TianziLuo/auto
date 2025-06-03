from playwright.sync_api import sync_playwright, TimeoutError

USERNAME = "9518010205"
PASSWORD = "Sandy168!"

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=False)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()

    page.goto("https://home.eccang.com/login?redirect=%2Fuser%2Fhome%3F")
    page.fill('input[id="userName"]', USERNAME)
    page.fill('input[id="password"]', PASSWORD)
    page.locator('span.home-ant-checkbox').click()
    page.locator('a.ec-login-submit').click()

    # 等待页面加载
    page.wait_for_load_state("networkidle")
    print("✅ 登录成功")



    input("🕒 脚本暂停，按 Enter 键退出...")
