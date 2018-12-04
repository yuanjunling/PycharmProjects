#coding=utf-8
import xlrd
from datetime import datetime
from xlrd import xldate_as_tuple
#路径前加 r，读取的文件路径
file_path = r'D:\test111.xls'
file_path1 ='D://test111.xls'
#文件路径的中文转码
file_path = file_path.decode('utf-8')
#获取数据
data = xlrd.open_workbook(file_path)
#获取sheet
table = data.sheet_by_name('Sheet1')
#获取总行数
nrows = table.nrows
#获取总列数
ncols = table.ncols
#获取一行的数值，例如第5行
rowvalue = table.row_values(0)
#获取一列的数值，例如第6列
col_values = table.col_values(1)
#获取一个单元格的数值，例如第1行第2列
cell_value = table.cell(0,0).value
print cell_value

def reacell_value(file_path,a,b):
    file_path = file_path.decode('utf-8')    # 文件路径的中文转码
    data = xlrd.open_workbook(file_path)# 获取数据
    cell_value = table.cell(a,b).value # 获取一个单元格的数值，例如第1行第2列
    return cell_value

fangfa = reacell_value(file_path,1,1)
print fangfa

# def readExcelDataByName(fileName, sheetName):
#     table = None
#     errorMsg = None
#     try:
#         data = xlrd.open_workbook(fileName)
#         table = data.sheet_by_index(sheetName)
#     except Exception, msg:
#         errorMsg = msg
#     return table, errorMsg

def rea_cell_value(file_path,a):
    file_path = file_path.decode('utf-8')    # 文件路径的中文转码
    data = xlrd.open_workbook(file_path)# 获取数据
    col_values = table.row_values(a) # 获取一个单元格的数值，例如第1行第2列
    return col_values
fangfa1 = rea_cell_value(file_path,1)
print str(fangfa1).decode("unicode_escape").encode("utf-8")