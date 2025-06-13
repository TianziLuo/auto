import os
import datetime
import win32com.client as win32

# File paths
file = r"C:\Frank\原始数据\店小秘+TP+订单+盘点\店小秘 盘点下载 源文件.xlsx"
xlsx_path = r'C:\Frank\2.2_店小秘.xlsx'

today = datetime.date.today()

def is_modified_today(file_path):
    try:
        # Check if the file exists and was modified today
        return os.path.isfile(file_path) and datetime.date.fromtimestamp(os.path.getmtime(file_path)) == today
    except Exception as e:
        print(f"❌ Error checking file modification time: {e}")
        return False

if is_modified_today(file):
    try:
        print("✅ File has been updated, opening Excel file...")

        excel = win32.gencache.EnsureDispatch('Excel.Application')
        excel.Visible = True  # Show Excel window
        excel.DisplayAlerts = True  # Allow alerts, so manual refresh prompts appear

        wb = excel.Workbooks.Open(xlsx_path)

        print("✅ Excel file is opened. Please refresh data manually.")

    except Exception as e:
        print(f"❌ Operation failed: {e}")
else:
    print("📌 File not updated today, skipping Excel launch.")

