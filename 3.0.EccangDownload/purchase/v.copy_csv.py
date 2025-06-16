import shutil
from pathlib import Path
from datetime import datetime, timedelta

# Source file path
source_file = Path(r"C:\Frank\合并文件\purchase_orders 合并.csv")

# Check if file was saved in the last 30 seconds
MAX_FILE_AGE  = datetime.fromtimestamp(source_file.stat().st_mtime)

if datetime.now() - MAX_FILE_AGE > timedelta(seconds=30):
    print(f"Skipped: '{source_file}' was last modified more than 30 seconds ago.")
else:
    # Target directory path
    target_dir = Path(r"C:\Frank\原始数据\易仓下载")

    # Create target directory if it doesn't exist
    target_dir.mkdir(parents=True, exist_ok=True)

    # Full path for the copied file in the target directory
    dest_file = target_dir / source_file.name

    # Copy the file to the target directory
    shutil.copy2(source_file, dest_file)

    print(f"Copied '{source_file}' to '{dest_file}'")
