import os
import datetime
import win32com.client as win32

# 文件路径
file1 = r'C:\Frank\原始数据\店小秘+TP+订单+盘点\新TP订单下载 order_report.csv'
file2 = r'C:\Frank\原始数据\店小秘+TP+订单+盘点\老TP订单下载 order_report.csv'
xlsx_path = r'C:\Frank\2.1_易仓管理.xlsx'

# 今天日期
today = datetime.date.today()

# 判断文件是否今天更新
def is_modified_today(file_path):
    return os.path.isfile(file_path) and datetime.date.fromtimestamp(os.path.getmtime(file_path)) == today

if is_modified_today(file1) and is_modified_today(file2):
    try:
        print("✅ 两个订单文件都已更新，正在打开 Excel 文件...")

        excel = win32.gencache.EnsureDispatch('Excel.Application')
        excel.Visible = True  # 显示 Excel 给用户看
        wb = excel.Workbooks.Open(xlsx_path)

        print("✅ Excel 文件已打开，请手动刷新或处理。")

    except Exception as e:
        print(f"❌ 操作失败：{e}")
else:
    print("📌 未检测到两个文件都为今日更新，跳过打开 Excel。")


