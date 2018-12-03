#coding=utf-8
import xlrd
from datetime import datetime
from xlrd import xldate_as_tuple
#路径前加 r，读取的文件路径
file_path = r'D:\test111.xls'
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

def fangfa(a=None,b=None):
    # 路径前加 r，读取的文件路径
    file_path = r'D:\test111.xls'
    # 文件路径的中文转码
    file_path = file_path.decode('utf-8')
    # 获取数据
    data = xlrd.open_workbook(file_path)
    # 获取sheet
    table = data.sheet_by_name('Sheet1')
    # 获取总行数
    nrows = table.nrows
    # 获取总列数
    ncols = table.ncols
    # 获取一个单元格的数值，例如第1行第2列
    cell_value = table.cell(a, b).value
    return cell_value
fangfa = fangfa(1,1)
print fangfa