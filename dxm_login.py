from playwright.sync_api import sync_playwright
import time

USERNAME = "annie515"
PASSWORD = "Annie1688!"

def login_to_dianxiaomi():
    with sync_playwright() as p:
        print("🚀 启动浏览器中...")
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(accept_downloads=True)
        page = context.new_page()

        try:
            # 只阻止字体加载，不影响验证码图片
            page.route("**/*", lambda route, request: route.abort()
                       if request.resource_type == "font"
                       else route.continue_())

            print("🌐 打开登录页面中...")
            page.goto("https://www.dianxiaomi.com/index.htm", timeout=60000, wait_until="domcontentloaded")

            print("📝 输入用户名和密码...")
            page.fill('input[placeholder="请输入用户名"]', USERNAME)
            page.fill('input[placeholder="请输入密码"]', PASSWORD)

            print("🔒 请手动输入验证码并点击登录按钮...")
            input("⏳ 验证码输入完并点击登录后，请按 Enter 继续...")

            # 等待网络空闲或页面加载完成
            page.wait_for_load_state("networkidle", timeout=30000)

            # 登录成功后跳转到指定页面
            print("🔄 跳转到目标页面...")
            page.goto("https://www.dianxiaomi.com/dxmWarehoseMaterialProduct/index.htm?pageState=1", timeout=30000)

            print("✅ 页面跳转成功，准备执行后续操作...")

            # TODO: 可在此添加后续自动化逻辑，比如点击导出按钮、筛选等
            time.sleep(5)

        except Exception as e:
            print("❌ 出现错误：", e)
        finally:
            browser.close()
            print("🔚 浏览器已关闭")

if __name__ == "__main__":
    login_to_dianxiaomi()
