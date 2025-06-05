import os
import shutil
from pathlib import Path

# Set source and target directories
source_dir = Path.home() / "Downloads"
target_dir = Path(r"C:\Frank\原始数据\店小秘+TP+订单+盘点")

# Ensure the target directory exists
target_dir.mkdir(parents=True, exist_ok=True)

# Keywords to search for
keywords = ["pandianshuju"]

# Desired new filename
new_filename = "店小秘 盘点下载 源文件.xlsx"

# Loop through keywords to find the latest matching file
for keyword in keywords:
    latest_file = None
    latest_mtime = 0

    # Walk through source directory
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".xlsx") and keyword in file:
                full_path = Path(root) / file
                mtime = full_path.stat().st_mtime
                if mtime > latest_mtime:
                    latest_mtime = mtime
                    latest_file = full_path

    # Copy and rename if found
    if latest_file:
        dest_path = target_dir / new_filename
        shutil.copy2(latest_file, dest_path)
        print(f"✅ Copied and renamed to: {dest_path}")
    else:
        print(f"⚠️ No file found containing '{keyword}'")
