import pandas as pd
import warnings

# 忽略 openpyxl 的无害警告
warnings.simplefilter("ignore", UserWarning)

# 文件路径
excel_path = r"C:\Frank\2.1_易仓管理.xlsx"
sheet_name = "易仓进TP"
csv_path = r"C:\Users\monica\Desktop\TP-Upload.csv"

# 读取 Excel（以字符串方式读取）
df = pd.read_excel(excel_path, sheet_name=sheet_name, dtype=str)
df = df.fillna('')

# 处理 Post Date 列（格式化为 M/D/YYYY）
if 'Post Date' in df.columns:
    try:
        df['Post Date'] = pd.to_datetime(df['Post Date'], errors='coerce') \
                            .apply(lambda x: f"{x.month}/{x.day}/{x.year}" if pd.notnull(x) else '')
    except Exception as e:
        print("日期格式化出错：", e)

# 保存为 CSV，纯文本格式
df.to_csv(csv_path, index=False, encoding='utf-8-sig', quoting=3)
