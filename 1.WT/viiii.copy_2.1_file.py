import os
from pathlib import Path
import shutil
from datetime import datetime

# 原始文件路径
source_path = r"C:\Frank\2.1_易仓管理.xlsx"

# 下载文件夹路径
download_dir = Path(os.path.expanduser('~')) / 'Downloads'

# 获取当前日期的 MMDD 格式
date_str = datetime.now().strftime('%m%d')

# 提取原文件名和扩展名
original_filename = Path(source_path).stem  # 文件名不含扩展名
extension = Path(source_path).suffix        # 文件扩展名，例如 .xlsx

# 构建新文件名
new_filename = f"{original_filename} {date_str}{extension}"
destination_path = download_dir / new_filename

# 执行复制操作
shutil.copy2(source_path, destination_path)

print(f"✅ 文件已复制到: {destination_path}")
