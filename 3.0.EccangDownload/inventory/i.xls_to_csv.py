import os
from pathlib import Path

# 设置目标文件夹路径
folder_path = Path.home() / "Downloads"

# 查找所有匹配的 .xls 文件
matched_files = []
for filename in os.listdir(folder_path):
    if "库存查询（库位）" in filename and filename.lower().endswith('.xls'):
        full_path = os.path.join(folder_path, filename)
        matched_files.append((full_path, os.path.getmtime(full_path)))

# 如果有匹配文件，找到最新的一个
if matched_files:
    # 根据修改时间排序（最新的排最后）
    matched_files.sort(key=lambda x: x[1], reverse=True)
    latest_file = matched_files[0][0]

    # 构造新文件路径（改为 .csv 后缀）
    new_path = os.path.splitext(latest_file)[0] + '.csv'

    try:
        os.rename(latest_file, new_path)
        print(f"✅ 最新文件已重命名为 CSV:\n{latest_file} → {new_path}")
    except Exception as e:
        print(f"❌ 重命名失败: {e}")
else:
    print("📌 没有找到包含“库存查询（库位）”的 .xls 文件")
