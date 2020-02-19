# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# 第三步：调用Seaborn绘制柱状图
#------------------------------------------------------------------------------
import time
import matplotlib
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt 

# 读取数据
n = time.strftime("%Y-%m-%d") + "-all.csv"
data = pd.read_csv(n)

# 设置窗口
fig, ax = plt.subplots(1,1)
print(data['province'])

# 设置绘图风格及字体
sns.set_style("whitegrid",{'font.sans-serif':['simhei','Arial']})

# 绘制柱状图
g = sns.barplot(x="province", y="confirm", data=data, ax=ax,
            palette=sns.color_palette("hls", 8))

# 在柱状图上显示数字
i = 0
for index, b in zip(list(data['province']), list(data['confirm'])):
    g.text(i+0.05, b+0.05, b, color="black", ha="center", va='bottom', size=6)
    i = i + 1

# 设置Axes的标题
ax.set_title('全国疫情最新情况')

# 设置坐标轴文字方向 
ax.set_xticklabels(ax.get_xticklabels(), rotation=-60)

# 设置坐标轴刻度的字体大小
ax.tick_params(axis='x',labelsize=8)
ax.tick_params(axis='y',labelsize=8)

plt.show()
