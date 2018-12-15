#-*-coding:utf-8-*-

import xlrd
import pymysql
from datetime import datetime
from xlrd import xldate_as_tuple
import os
import tkinter.filedialog  # Python自带GUI库

db = pymysql.connect("localhost", "root", "zgsxhm", "db_0221", use_unicode=True, charset="utf8")


def write_database(database, sql):
    cursor = database.cursor()  # 使用 cursor() 方法创建一个游标对象 curs
    try:
        cursor.execute(sql)
    except Exception as e:
        database.rollback()  # 发生错误时回滚
        print(str(e))
    else:
        database.commit()  # 事务提交
        print('事务处理成功')

def get_datas(database, sql):
    cursor = database.cursor()  # 使用 cursor() 方法创建一个游标对象 curs
    try:
        cursor.execute(sql)
    except Exception as e:
        database.rollback()  # 发生错误时回滚
        print(str(e))
    else:
        database.commit()  # 事务提交
        datas = cursor.fetchall()
        cursor.close()
        return datas

# 文件对话框：
default_dir = r"文件路径"
f_name = tkinter.filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser((default_dir))))

# 取得这个Excel表
data = xlrd.open_workbook(f_name)
table = data.sheet_by_index(0)

dateStr = f_name[-18:-10]
date = datetime.strptime(dateStr, '%Y%m%d')

# 需要读取的位置（有点简陋）
begin_row = [5, 37]
side = ["买入", "卖出"]

for i in range(0, 2):
    for nrows_one in range(begin_row[i], begin_row[i] + 11):
        for ncols_one in range(1, table.ncols-1):
            inst_type = table.cell_value(nrows_one, 0).strip()
            bond_class = table.cell_value(4, ncols_one).strip()
            vol = table.cell_value(nrows_one, ncols_one)
            if (vol == "—"):
                vol = 0

            sql_insert = "insert into bytype(date, inst_type, side, bond_class, vol) values ('%s','%s','%s','%s','%f')" % \
                  (date, inst_type, side[i], bond_class, vol)
            write_database(db, sql_insert),



