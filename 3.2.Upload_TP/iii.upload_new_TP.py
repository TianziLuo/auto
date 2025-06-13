from playwright.sync_api import sync_playwright
from playwright.sync_api import sync_playwright, expect
import time

USERNAME = "wayfaircolourtree"
EMAIL = "wayfair.colourtree@gmail.com"
PASSWORD = "Colourtree168!!"  

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=chrome_path, headless=False)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()

    # login
    page.goto("https://www.teapplix.com/auth/")
    page.fill('input[placeholder="账户名"]', USERNAME)
    page.fill('input[placeholder="登录电子邮件"]', EMAIL)
    page.fill('input[placeholder="密码"]', PASSWORD)

    page.click('button.ant-btn-primary')
    page.wait_for_load_state("networkidle")
    print("✅ 登录成功")

    #Inventory 
    page.get_by_text("Inventory", exact=True).click()
    page.wait_for_selector('text=Quantity', timeout=10000)
    page.get_by_text("Quantity", exact=True).nth(0).click()
    print("✅ 成功点击 Quantity")

    # Import/Export
    page.get_by_text("Import/Export", exact=True).click()
    page.wait_for_selector("text=Reject entire import", timeout=10000)
    page.get_by_text("Reject entire import", exact=True).click()

    # upload
    page.set_input_files('input[type="file"]', r"C:\Users\monica\Downloads\TP-Upload.csv")

    time.sleep(1)
    # import file
    page.get_by_text("Import CSV", exact=True).click()
    page.wait_for_selector("text=Import CSV", timeout=10000)
    input("🟢 文件上传完成，按 Enter 关闭浏览器...")
    browser.close()


