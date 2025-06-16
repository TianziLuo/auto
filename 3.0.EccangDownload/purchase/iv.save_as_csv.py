import pandas as pd
import csv  
from pathlib import Path
from datetime import datetime, timedelta

# Path to the Excel input file
source_file = Path(r'C:\Frank\合并文件\purchase_orders 合并.xlsx')

# Path to the output CSV file
csv_file = Path(r'C:\Frank\合并文件\purchase_orders 合并.csv')

# Check if source file was modified within the last 30 seconds
MAX_FILE_AGE = datetime.fromtimestamp(source_file.stat().st_mtime)

if datetime.now() - MAX_FILE_AGE > timedelta(seconds=30):
    print(f"Skipped: '{source_file}' was last modified more than 30 seconds ago.")
else:
    # Read the Excel file (default: first worksheet)
    df = pd.read_excel(source_file)

    # Export to CSV with specified settings
    df.to_csv(
        csv_file,
        index=False,
        encoding='utf-8-sig',
        lineterminator='\r\n',
        quoting=csv.QUOTE_ALL
    )
    print(f"Converted '{source_file}' to '{csv_file}'")

