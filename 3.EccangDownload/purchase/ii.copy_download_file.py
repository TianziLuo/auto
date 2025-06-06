import os
import shutil
from pathlib import Path
from datetime import datetime

# Set source and target directories
download_dir = Path(os.path.expanduser('~')) / 'Downloads'
target_dir = Path(r"C:\Frank\合并文件\易仓采购单管理")

# Create target directory if it doesn't exist
target_dir.mkdir(parents=True, exist_ok=True)

# List of keywords to search for in file names
keywords = ["purchase_orders"]

today_files = []
today_date = datetime.today().date()  # Today's date (without time)

# Walk through the download directory
for root, _, files in os.walk(download_dir):
    for file in files:
        # Check if file ends with '.csv' and contains any of the keywords
        if file.endswith(".csv") and any(k in file for k in keywords):
            full_path = Path(root) / file
            # Get file's last modified date
            mtime = datetime.fromtimestamp(full_path.stat().st_mtime).date()
            # If modified date is today, add to the list
            if mtime == today_date:
                today_files.append(full_path)

# If matching files are found, copy t
