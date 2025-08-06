
import matplotlib.pyplot as plt
plt.rc('font', family='Times New Roman')

import numpy as np
from matplotlib.ticker import FuncFormatter

# 数据
datasets = ['Gibson', 'MP3D', 'HM3D']
# SR数据
sr_method_a = [0.917, 0.791, 0.791]
sr_method_b = [0.741, 0.635, 0.620]
# SPL数据
spl_method_a = [0.685, 0.528, 0.466]
spl_method_b = [0.489, 0.371, 0.320]

# 设置柱状图参数
x = np.arange(len(datasets))  # 横坐标位置
width = 0.4  # 柱状图宽度

# 创建并列子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))

# 绘制SR子图
bars1_sr = ax1.bar(x - width/2, sr_method_a, width, label='w/o randomly augment', color='skyblue')
bars2_sr = ax1.bar(x + width/2, sr_method_b, width, label='w/ randomly augment', color='silver')

# 绘制SPL子图
bars1_spl = ax2.bar(x - width/2, spl_method_a, width, label='w/o randomly augment', color='skyblue')
bars2_spl = ax2.bar(x + width/2, spl_method_b, width, label='w/ randomly augment', color='silver')

# 设置SR子图
ax1.set_ylabel('Success Rate (SR) %', fontsize=30)
ax1.set_xticks(x)
ax1.set_xticklabels(datasets, fontsize=32)
ax1.tick_params(axis='y', labelsize=32)
ax1.yaxis.grid(True, linestyle='--', linewidth=1, alpha=0.7)
ax1.set_axisbelow(True)
ax1.set_ylim(0.4, 1.0)

# 设置SPL子图
ax2.set_ylabel('Success weighted by Path Length (SPL) %', fontsize=30)
ax2.set_xticks(x)
ax2.set_xticklabels(datasets, fontsize=32)
ax2.tick_params(axis='y', labelsize=32)
ax2.yaxis.grid(True, linestyle='--', linewidth=1, alpha=0.7)
ax2.set_axisbelow(True)
ax2.set_ylim(0.2, 0.8)

# 设置百分比格式
def to_percentage(value, _):
    return f'{value * 100:.1f}'
ax1.yaxis.set_major_formatter(FuncFormatter(to_percentage))
ax2.yaxis.set_major_formatter(FuncFormatter(to_percentage))

# 添加数值标签
def add_labels(ax, bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height*100:.1f}%',
                   xy=(bar.get_x() + bar.get_width() / 2, height),
                   xytext=(0, 3),
                   textcoords="offset points",
                   ha='center', va='bottom', fontsize=32)

add_labels(ax1, bars1_sr)
add_labels(ax1, bars2_sr)
add_labels(ax2, bars1_spl)
add_labels(ax2, bars2_spl)

# 设置边框
for ax in [ax1, ax2]:
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1.5)

# 为两个子图都添加图例
legend_params = {
    'fontsize': 30,
    'loc': 'upper right',
    'frameon': True,
    'edgecolor': 'black',
    'borderpad': 0.8
}

ax1.legend(**legend_params)
ax2.legend(**legend_params)
# plt.subplots_adjust(top=0.85, wspace=0.3)
# 调整布局
plt.tight_layout()
plt.subplots_adjust(top=0.85, wspace=0.3)
# 保存和显示图形
plt.savefig('figure_SR_SPL.pdf', format='pdf', bbox_inches='tight', dpi=900)
plt.show()

