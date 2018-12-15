#-*-coding:utf-8-*-

import pandas as pd
import pymysql
from datetime import datetime
import pandas.io.sql as pds
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
import matplotlib.patches as patches
import numpy as np
from matplotlib.font_manager import FontProperties


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

# 设置daba base, sql, 读取data
db = pymysql.connect("localhost", "root", "zgsxhm", "db_0221", use_unicode=True, charset="utf8")
sql_get_datas = 'select * from bytype '
data = pds.read_sql(sql_get_datas, db)

bond_class_series = data['bond_class'].drop_duplicates()
inst_list = data['inst_type'].drop_duplicates().values
inst_list.sort()
N_BOND_CLASS = len(bond_class_series)
N_INST = len(data['inst_type'].drop_duplicates())
N_INST_range = range(N_INST)

# 配置figure
# 配置字体
font_set = FontProperties(fname="c:/myproject/pyExcel/cfets_reports/simfang.ttf", size=12)
# 配置颜色
jet = cm = plt.get_cmap('jet')
cNorm = colors.Normalize(vmin=0, vmax=N_INST_range[-1])
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=jet)
colorVal = []
# 生成图例中的不同颜色marker
legend_patch = []

for idx in N_INST_range:
    colorVal.append(scalarMap.to_rgba(idx))
    legend_patch.append(patches.Patch(color=scalarMap.to_rgba(idx), label=inst_list[idx]))

# 生成figure和子图
fig, axes = plt.subplots(3, 3, figsize=(12,8))
# 绘制axes
for i in range(3):
    for j in range(3):
        bond_class = bond_class_series[i*3+j]
        # 通过数据透视表取用数据
        d1 = pd.pivot_table(data[(data.bond_class == bond_class)], index=["inst_type"], values=["vol"],
                            columns=["side"], aggfunc=np.sum)

        axes[i][j].set_title("%s" % bond_class, fontproperties=font_set)
        # 绘制柱状图, 向上、向下、和实心柱状
        x = np.arange(N_INST)
        axes[i][j].bar(x, np.array(d1.values[:, 0]), facecolor='white', edgecolor=colorVal)
        axes[i][j].bar(x, -np.array(d1.values[:, 1]), facecolor='white', edgecolor=colorVal)
        axes[i][j].bar(x, np.array(d1.values[:, 0]) - np.array(d1.values[:, 1]), color=colorVal)
        # x轴设置为空
        axes[i][j].set_xticks([])

# 绘制图例
axes[0][0].legend(handles=legend_patch,
                  bbox_to_anchor=(-0.2, 1.12, 3.5, .1),
                  loc='lower center',
                  ncol=6,
                  mode='expand',
                  borderaxespad=0.,
                  prop=font_set
                  )

# 增加标题，通过增加一个没有面积的ax的方式
ax = plt.subplot(111, position=[0,0.05,1,0], xticks=[])
ax.set_title('图：各类机构不同债券品种的交易情况', fontproperties=font_set)

plt.savefig('C:/myproject/pyExcel/cfets_reports/bar.png')
plt.show()


