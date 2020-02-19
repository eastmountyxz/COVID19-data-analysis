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
data = pd.read_csv("2020-02-13-all-4db-2no.csv")

# 设置窗口
fig, ax = plt.subplots(1,1)
print(data['province'])

# 设置绘图风格及字体
sns.set_style("whitegrid",{'font.sans-serif':['simhei','Arial']})

# 绘制柱状图
g = sns.barplot(x="province", y="data", hue="tpye", data=data, ax=ax,
            palette=sns.color_palette("hls", 8))
    
# 设置Axes的标题
ax.set_title('全国疫情最新情况')

# 设置坐标轴文字方向 
ax.set_xticklabels(ax.get_xticklabels())

# 设置坐标轴刻度的字体大小
ax.tick_params(axis='x',labelsize=8)
ax.tick_params(axis='y',labelsize=8)

plt.show()
