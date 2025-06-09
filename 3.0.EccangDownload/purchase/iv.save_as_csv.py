import pandas as pd
import csv  # For setting quoting options

# Path to the Excel input file
excel_path = r'C:\Frank\合并文件\purchase_orders 合并.xlsx'

# Path to the output CSV file
csv_path = r'C:\Frank\合并文件\purchase_orders 合并.csv'

# Read the Excel file (default: first worksheet)
df = pd.read_excel(excel_path)

# Export to CSV with the following settings:
# - UTF-8 with BOM encoding: ensures Excel displays Chinese characters correctly
# - Windows-style line endings (\r\n): compatible with Excel
# - Quote all fields: prevents issues with commas, dates, or special characters
df.to_csv(
    csv_path,
    index=False,
    encoding='utf-8-sig',
    lineterminator='\r\n',
    quoting=csv.QUOTE_ALL
)
