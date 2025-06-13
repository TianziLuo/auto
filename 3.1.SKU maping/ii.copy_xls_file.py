import shutil
from pathlib import Path

# Source file path
source_file = Path(r"C:\Users\monica\Downloads\上传易仓SKU映射关系.xls")

# Target directory path
target_dir = Path(r"C:\Frank\易仓-TP")

# Full path for the copied file in the target directory
dest_file = target_dir / source_file.name

# Copy the file to the target directory
shutil.copy2(source_file, dest_file)

print(f"Copied '{source_file}' to '{dest_file}'")
