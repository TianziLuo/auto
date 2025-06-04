import os
import datetime

# Target folder
folder_path = r'C:\Frank\原始数据\1.6 日报AMZ FBA Fee Preview 店名csv'

# Target file names (case-sensitive)
target_files = ['CT.CSV', 'SM.CSV', 'AG.CSV', 'RS.CSV']

# Today's date in YYYY-MM-DD format
date_suffix = datetime.date.today().isoformat()

# Process each target file
for file_name in target_files:
    original_path = os.path.join(folder_path, file_name)
    
    if os.path.exists(original_path):
        # New filename: original name without extension + '备用' + date + .csv
        name_without_ext = os.path.splitext(file_name)[0]
        new_file_name = f"{name_without_ext} 备用 {date_suffix}.csv"
        new_path = os.path.join(folder_path, new_file_name)
        
        try:
            os.rename(original_path, new_path)
            print(f"Renamed: {file_name} -> {new_file_name}")
        except Exception as e:
            print(f"Failed to rename {file_name}, Reason: {e}")
    else:
        print(f"File not found: {file_name}")