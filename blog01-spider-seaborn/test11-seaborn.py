# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# 第四步：调用Seaborn绘制其他图形
#------------------------------------------------------------------------------
import time
import matplotlib
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt 

# 读取数据
data = pd.read_csv('2020-02-19-all.csv')

plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    #用来正常显示负号

# 设置窗口
fig, ax = plt.subplots(1,1)
print(data['province'])

# 设置Axes的标题
ax.set_title('全国疫情最新情况')

# 设置坐标轴刻度的字体大小
ax.tick_params(axis='x',labelsize=8)
ax.tick_params(axis='y',labelsize=8)

# 设置绘图风格及字体
sns.set_style("whitegrid",{'font.sans-serif':['simhei','Arial']})

# 六角形
#sns.jointplot(x="dead", y="heal", data=data, color="b", kind='hex')

# KDE 图
sns.jointplot(x="dead", y="heal", data=data, kind="kde", space=0, color="#6AB27B")

# 散点图+KDE 图
# g = (sns.jointplot(x="dead", y="heal", data=data, color="k").plot_joint(sns.kdeplot, zorder=0, n_levels=6))

plt.show()
