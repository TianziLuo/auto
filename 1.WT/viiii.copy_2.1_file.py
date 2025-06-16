import os
from pathlib import Path
import shutil
from datetime import datetime, timedelta
import sys   # Used for early script exit

# —————— Configuration ——————
# Source file
source_path = r"C:\Frank\2.1_易仓管理.xlsx"

# Target directory
download_dir = Path(os.path.expanduser('~')) / 'Downloads'

# Maximum allowed time interval 
MAX_FILE_AGE = 30 

# 1) Check that the source file exists
if not Path(source_path).is_file():
    sys.exit(f"❌ Source file not found: {source_path}")

# 2) Verify the file’s last‑modified time
mtime = datetime.fromtimestamp(os.path.getmtime(source_path))
now   = datetime.now()

if now - mtime > timedelta(seconds=MAX_FILE_AGE):
    # Too old — abort the copy
    seconds_ago = int((now - mtime).total_seconds())
    sys.exit(
        f"⚠️ Last saved {seconds_ago} seconds ago, "
        f"exceeding the {MAX_FILE_AGE}‑second limit; copy aborted."
    )

# 3) Build the destination filename
date_str  = now.strftime('%m%d')           # Current date in MMDD format
stem      = Path(source_path).stem         # Filename without extension
extension = Path(source_path).suffix       # File extension 
new_name  = f"{stem} {date_str}{extension}"
dest_path = download_dir / new_name

# 4) Perform the copy
shutil.copy2(source_path, dest_path)

print(f"✅ File copied to: {dest_path}")
