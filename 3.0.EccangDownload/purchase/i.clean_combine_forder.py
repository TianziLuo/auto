import os
import glob

# List of target folder paths
folder_paths = [
    r'C:\Frank\合并文件\易仓采购单管理',
]

# File types to delete
file_patterns = ['*.xlsx', '*.csv']

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

