from playwright.sync_api import sync_playwright, TimeoutError

USERNAME = "9518010205"
PASSWORD = "Sandy168!"

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=False)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()

    # 登录
    page.goto("https://home.eccang.com/login?redirect=%2Fuser%2Fhome%3F")
    page.fill('input[id="userName"]', USERNAME)
    page.fill('input[id="password"]', PASSWORD)
    page.locator('span.home-ant-checkbox').click()
    page.locator('a.ec-login-submit').click()

    page.wait_for_load_state("networkidle")
    print("✅ 登录成功")

    # 跳转到目标页面（含 iframe）
    page.goto("https://home.eccang.com/entry/EY1LJS/ERP/iframe#/m_45619")
    page.wait_for_load_state("networkidle")

    # 等待 iframe 出现
    page.wait_for_selector("iframe#m_48158")

    # 获取 iframe 元素
    iframe_element = page.locator("iframe#m_48158")

    # ✅ 获取 Frame 对象
    frame = iframe_element.content_frame()

    if frame is None:
        print("❌ iframe 内容尚未加载，frame is None")
    else:
        # ✅ 等待并点击 iframe 内的按钮
        frame.wait_for_selector("#createceiveButton", state="visible", timeout=10000)
        frame.click("#createceiveButton")
        print("✅ 成功点击按钮")

    input("🕒 脚本暂停，按 Enter 键退出...")
