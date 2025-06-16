import os
import shutil
from pathlib import Path

# Set source and target directories
download_dir = Path(os.path.expanduser('~')) / 'Downloads'
target_dir1 = Path(r"C:\Frank\易仓-TP")
target_dir2 = Path(r"C:\ACT\公用核心\upload_1.1 TP 库存更新")

# Keywords to search for in file names
keywords = ["TP"]

# Loop through each keyword to find the latest matching file
for keyword in keywords:
    latest_file = None
    latest_mtime = 0

    # Walk through the directory tree
    for root, _, files in os.walk(download_dir):
        for file in files:
            # Check if file is .csv and contains the keyword
            if file.endswith(".csv") and keyword in file:
                full_path = Path(root) / file
                mtime = full_path.stat().st_mtime
                # Keep the most recently modified matching file
                if mtime > latest_mtime:
                    latest_mtime = mtime
                    latest_file = full_path

    # If a matching file was found, copy it to the target folder
    if latest_file:
        dest_path1 = target_dir1 / latest_file.name
        dest_path2 = target_dir2/ latest_file.name
        shutil.copy2(latest_file, dest_path1)
        shutil.copy2(latest_file, dest_path2)
        print(f"✅ 已复制到:\n→ {target_dir1}\n→ {target_dir2}")
    else:
        print(f"⚠️ No file found containing '{keyword}'")

