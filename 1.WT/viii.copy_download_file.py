import os
import shutil
from pathlib import Path

# Set source and target directories
download_dir = Path(os.path.expanduser('~')) / 'Downloads'
target_dir = Path(r"C:\Frank\易仓-TP\无小票发货 Sarah")

# Create target directory if it doesn't exist
target_dir.mkdir(parents=True, exist_ok=True)

# Keywords to search for in file names
keywords = ["Use"]

# Loop through each keyword to find the latest matching file
for keyword in keywords:
    latest_file = None
    latest_mtime = 0

    # Walk through the directory tree
    for root, _, files in os.walk(download_dir):
        for file in files:
            # Check if file is .xlsx and contains the keyword
            if file.endswith(".csv") and keyword in file:
                full_path = Path(root) / file
                mtime = full_path.stat().st_mtime
                # Keep the most recently modified matching file
                if mtime > latest_mtime:
                    latest_mtime = mtime
                    latest_file = full_path

    # If a matching file was found, copy it to the target folder
    if latest_file:
        dest_path = target_dir / latest_file.name
        shutil.copy2(latest_file, dest_path)
        print(f"✅ Copied: {latest_file.name} to {target_dir}")
    else:
        print(f"⚠️ No file found containing '{keyword}'")

