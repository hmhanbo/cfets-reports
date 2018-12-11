import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
import numpy as np
import matplotlib.patches as patches
from matplotlib.font_manager import FontProperties


n = np.array([0,1,2,3,4,5])
font_set = FontProperties(fname="c:/myproject/pyExcel/cfets_reports/simfang.ttf", size=12)
fig, axes = plt.subplots(3, 3)
ax = fig.add_subplot(pos=[0,0.05,1,0.1])
# plt.figure(1, clear=True)


# ax.set_title('图：各类对不同债券品种的交易情况', fontproperties=font_set)
# jet = cm = plt.get_cmap('jet')
# cNorm = colors.Normalize(vmin=0, vmax=3)
# scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=jet)
# colorVal = []
#
# red_patch = []
# for idx in range(4):
#     colorVal.append(scalarMap.to_rgba(idx))
#     red_patch.append(patches.Patch(color=scalarMap.to_rgba(idx), label='汉字'))

# for i in range(1, 4):
#     for j in range(3):
#         print(type(axes[i][j]))
#         axes[i][j].bar(n, n**2, align="center", width=0.5, alpha=0.5)
#         axes[i][j].set_title("bar")

# ax = plt.subplot(411)
# ax.set_title('legend')
# ax.legend(handles=red_patch,
#           bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
#           ncol=3,
#           mode="expand",
#           borderaxespad=0.,
#           prop=font_set
#           )
# axes[0][0].legend(handles=red_patch,
#                   bbox_to_anchor=(0.3, 0.95, 3, .102), loc='lower left',
#                   ncol=3,
#                   mode="expand",
#                   borderaxespad=0.,
#                   prop=font_set
#                   )
# axes[0][0].set_xticks([])
# ax = plt.subplot(111, position=[0,0,1,0], xticks=[])
# frameon=False, visible=False

# axes[1][1].add_patch(
#     patches.Rectangle(
#         (0.1, 0.1),   # (x,y)
#         0.5,          # width
#         0.5,          # height
#         facecolor=(0.5, 0.5, 0.5)
#     )
# )


plt.show()
