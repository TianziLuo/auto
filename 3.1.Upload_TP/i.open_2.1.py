import win32com.client as win32

# 文件路径
xlsx_path = r'C:\Frank\2.1_易仓管理.xlsx'

# 获取 Excel 应用对象
excel = win32.gencache.EnsureDispatch('Excel.Application')
excel.Visible = True  # 显示 Excel 给用户看

# 打开工作簿
wb = excel.Workbooks.Open(xlsx_path)

print("✅ Excel 文件已打开，请手动刷新或处理。")
