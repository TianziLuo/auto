import shutil
from pathlib import Path

# 源文件路径
source_file = Path(r"C:\Users\monica\Downloads\店小秘 更新库存.xlsx")

# 目标文件夹路径（注意：是文件夹，不包含文件名）
target_dir1 = Path(r"C:\Frank\原始数据\店小秘+TP+订单+盘点")
target_dir2 = Path(r"C:\ACT\公用核心\Upload_2.1 店小秘  库存更新")

# 创建目标文件夹（如果不存在）
target_dir1.mkdir(parents=True, exist_ok=True)
target_dir2.mkdir(parents=True, exist_ok=True)

# 拼接完整目标文件路径
dest_file_1 = target_dir1 / source_file.name
dest_file_2 = target_dir2 / source_file.name

# 执行复制操作
shutil.copy2(source_file, dest_file_1)
shutil.copy2(source_file, dest_file_2)

print(f"✅ 已复制到:\n→ {dest_file_1}\n→ {dest_file_2}")
