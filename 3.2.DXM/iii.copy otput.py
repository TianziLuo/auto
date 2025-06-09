import shutil
from pathlib import Path

# Source file path
source_file = Path(r"C:\Frank\原始数据\店小秘+TP+订单+盘点\店小秘 更新库存.xlsx")

# Target directory path
target_dir = Path(r"C:\ACT\公用核心\Upload_2.1 店小秘  库存更新")

# Create target directory if it doesn't exist
target_dir.mkdir(parents=True, exist_ok=True)

# Full path for the copied file in the target directory
dest_file = target_dir / source_file.name

# Copy the file to the target directory
shutil.copy2(source_file, dest_file)

print(f"Copied '{source_file}' to '{dest_file}'")
