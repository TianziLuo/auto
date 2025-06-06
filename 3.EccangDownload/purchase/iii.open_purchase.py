import os
import datetime
import win32com.client as win32

# Folder and Excel file paths
folder_path = r'C:\Frank\合并文件\易仓采购单管理'
xlsx_path = r"C:\Frank\合并文件\purchase_orders 合并.xlsx"

# Today's date
today = datetime.date.today()

# Check if the file exists, is not empty, and was modified today
def is_nonempty_and_modified_today(file_path):
    return (
        os.path.isfile(file_path)
        and os.path.getsize(file_path) > 0
        and datetime.date.fromtimestamp(os.path.getmtime(file_path)) == today
    )

# Check if any file in the folder meets the criteria
def folder_has_updated_file(folder_path):
    if not os.path.isdir(folder_path):
        return False
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if is_nonempty_and_modified_today(file_path):
            return True
    return False

# Main logic
if folder_has_updated_file(folder_path):
    try:
        print("✅ A non-empty file updated today was found. Opening the Excel file...")

        excel = win32.gencache.EnsureDispatch('Excel.Application')
        excel.Visible = True
        wb = excel.Workbooks.Open(xlsx_path)

        print("✅ Excel file opened successfully. Please refresh or process manually.")

    except Exception as e:
        print(f"❌ Operation failed: {e}")
else:
    print("📌 No non-empty files updated today were found. Skipping Excel launch.")
