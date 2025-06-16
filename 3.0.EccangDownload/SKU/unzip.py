import os
import zipfile
from pathlib import Path
from datetime import datetime

# 默认下载目录
DOWNLOAD_DIR = Path.home() / "Downloads"

# 今天的日期
today = datetime.today().date()

# 包含的关键词
KEYWORDS = ["已映射", "未映射"]

def get_today_keyword_zip_files(folder):
    matched = []
    for zip_file in folder.glob("*.zip"):
        # 包含关键词
        if not any(keyword in zip_file.name for keyword in KEYWORDS):
            continue
        # 修改时间是今天
        mtime = datetime.fromtimestamp(zip_file.stat().st_mtime).date()
        if mtime == today:
            matched.append(zip_file)
    return matched

def unzip_file(zip_path, extract_to):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print(f"✅ 解压完成: {zip_path.name} -> {extract_to}")
    except zipfile.BadZipFile:
        print(f"❌ 错误: {zip_path.name} 不是有效的 zip 文件")

def main():
    print(f"📁 正在扫描目录: {DOWNLOAD_DIR}")
    zip_files = get_today_keyword_zip_files(DOWNLOAD_DIR)

    if not zip_files:
        print("⚠️ 没有符合条件的 zip 文件")
        return

    for zip_file in zip_files:
        unzip_file(zip_file, DOWNLOAD_DIR)

if __name__ == "__main__":
    main()
