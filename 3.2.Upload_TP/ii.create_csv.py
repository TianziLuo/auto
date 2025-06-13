import os
import pandas as pd

# 路径设置
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
csv_path = os.path.join(downloads_path, "TP-Upload.csv")

# Excel 源路径和 sheet 名
source_path = r"C:\Frank\2.1_易仓管理.xlsx"
sheet_name = "易仓进TP"

# 模板 CSV 路径
template_path = r"c:\Template\TP-Upload.csv"

# 读取 Excel（跳过第一行，只读 A-F列）
df_excel = pd.read_excel(source_path, sheet_name=sheet_name, header=None, skiprows=1, usecols="A:F")

# 去掉全为空的行
df_excel = df_excel.dropna(how='all')

# 防止第二列被 Excel 识别成日期（加上 '）
if df_excel.shape[1] >= 2:
    df_excel.iloc[:, 1] = df_excel.iloc[:, 1].apply(lambda x: f"'{x}" if pd.notna(x) else x)

# 读取模板 CSV，只保留第一行（通常是表头）
with open(template_path, "r", encoding="utf-8") as f:
    first_line = f.readline().strip()

# 写入新 CSV 文件
with open(csv_path, "w", encoding="utf-8", newline="") as f:
    f.write(first_line + "\n")
    df_excel.to_csv(f, index=False, header=False)

print(f"✅ 成功生成 CSV 文件：{csv_path}")
