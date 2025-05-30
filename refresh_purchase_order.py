import os
import datetime
import pandas as pd

# Define paths
source_folder = r'C:\Frank\合并文件\易仓采购单管理'
xlsx_path = r'C:\Frank\合并文件\purchase_orders 合并.xlsx'
csv_path = r'C:\Frank\合并文件\purchase_orders 合并.csv'

# Today's date
today = datetime.date.today()

# Check if folder is not empty and contains any file modified today
should_refresh = False
if os.path.isdir(source_folder):
    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name)
        if os.path.isfile(file_path):
            modified_date = datetime.date.fromtimestamp(os.path.getmtime(file_path))
            if modified_date == today:
                should_refresh = True
                break

# If condition is met, refresh and convert to CSV
if should_refresh:
    try:
        # Read Excel (you can add sheet_name='Sheet1' if needed)
        df = pd.read_excel(xlsx_path)
        
        # Save as CSV (UTF-8 encoding)
        df.to_csv(csv_path, index=False, encoding='utf-8-sig')

        print("Excel file refreshed and saved as CSV.")
    except Exception as e:
        print(f"Failed to read or save file: {e}")
else:
    print("No update needed — either folder is empty or no file was modified today.")