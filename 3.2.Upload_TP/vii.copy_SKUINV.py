import shutil
from pathlib import Path

# 源文件路径
source_file = Path(r"C:\Frank\易仓-TP\SKUINV.xlsx")

# 目标文件夹路径（注意：是文件夹，不包含文件名）
target_dir = Path(r"\\MICHAEL\ctshippingapp\SHIPDOC\INVUPLOAD")

# 创建目标文件夹（如果不存在）
target_dir.mkdir(parents=True, exist_ok=True)

# 拼接完整目标文件路径
dest_file = target_dir / source_file.name

# 执行复制操作
shutil.copy2(source_file, dest_file)

print(f"✅ 已复制到:\n→ {dest_file}")
