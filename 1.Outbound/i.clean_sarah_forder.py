import os
import glob

# Target folder path
folder_path = r'C:\Frank\易仓-TP\无小票发货 Sarah'

# Get all .xlsx and .csv files in the folder
file_patterns = ['*.xlsx', '*.csv']
files_to_delete = []

for pattern in file_patterns:
    files_to_delete.extend(glob.glob(os.path.join(folder_path, pattern)))

# Delete each file
for file in files_to_delete:
    try:
        os.remove(file)
        print(f"Deleted: {file}")
    except Exception as e:
        print(f"Failed to delete: {file}, Reason: {e}")

# Open the folder in File Explorer
os.startfile(folder_path)