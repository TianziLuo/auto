import os
import zipfile
import shutil
from pathlib import Path
from datetime import datetime

# ====== 路径配置 ======
DOWNLOAD_DIR = Path.home() / "Downloads"               # 默认下载目录
DEST_DIR = Path(r"C:\Frank\原始数据\易仓下载")            # 额外复制目的地

# ====== 过滤条件 ======
today = datetime.today().date()
KEYWORDS = ["已映射", "未映射"]

def get_today_keyword_zip_files(folder: Path):
    """找出今天下载且包含指定关键词的 zip 文件"""
    for zip_file in folder.glob("*.zip"):
        if not any(k in zip_file.name for k in KEYWORDS):
            continue
        if datetime.fromtimestamp(zip_file.stat().st_mtime).date() == today:
            yield zip_file

def unzip_and_copy(zip_path: Path):
    """解压 zip 到下载目录原位，并把文件再复制一份到 DEST_DIR"""
    print(f"▶ 处理: {zip_path.name}")

    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(DOWNLOAD_DIR)            # 先原位解压

        for member in z.namelist():          # 再把每个成员复制到目标目录
            src = DOWNLOAD_DIR / member
            if src.is_dir():                 # 目录本身不用复制；下面复制文件时会顺带创建目录
                continue
            dst = DEST_DIR / member
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

    print(f"✅ 已解压并复制到 {DEST_DIR}")

def main():
    print(f"📁 扫描目录: {DOWNLOAD_DIR}")
    zips = list(get_today_keyword_zip_files(DOWNLOAD_DIR))
    if not zips:
        print("⚠️ 没有符合条件的 zip")
        return

    DEST_DIR.mkdir(parents=True, exist_ok=True)   # 确保目标路径存在
    for z in zips:
        unzip_and_copy(z)

