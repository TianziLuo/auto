import os
import glob

# List of target folder paths
folder_paths = [
    r'C:\Frank\原始数据\1.1 日报AMZ Amazon fulfilled Inventory 店名csv',
    r'C:\Frank\原始数据\1.2 日报AMZ All Orders 30Day 店名txt',
    r'C:\Frank\原始数据\1.3 日报AMZ Manage Inventory 店名csv',
    r'C:\Frank\原始数据\1.4 日报AMZ Reserved Inventory 店名csv'
]

# File types to delete
file_patterns = ['*.xlsx', '*.csv','*.txt']

# Process each folder
for folder_path in folder_paths:
    print(f"\nProcessing folder: {folder_path}")

    files_to_delete = []
    for pattern in file_patterns:
        files_to_delete.extend(glob.glob(os.path.join(folder_path, pattern)))

    for file in files_to_delete:
        try:
            os.remove(file)
            print(f"Deleted: {file}")
        except Exception as e:
            print(f"Failed to delete: {file}, Reason: {e}")

