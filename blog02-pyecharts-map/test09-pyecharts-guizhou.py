# -*- coding: utf-8 -*-
import time, json, requests
import pandas as pd
from pyecharts.charts import Bar
import pyecharts.options as opts

#-------------------------------------------------------------------------------------
# 第一步：读取数据
#-------------------------------------------------------------------------------------
n = time.strftime("%Y-%m-%d") + "-gz.csv"
data = pd.read_csv(n)
province_list = list(data['province'])
confirm_list = list(data['confirm'])
dead_list = list(data['dead'])
heal_list = list(data['heal'])
new_confirm_list = list(data['new_confirm'])
print(province_list)                    # 地区
print(confirm_list)                     # 确诊数据
print(dead_list)                        # 死亡数据
print(heal_list)                        # 治愈数据
print(new_confirm_list)                 # 新增确诊


#-------------------------------------------------------------------------------------
# 第二步：绘制贵州柱状图
#-------------------------------------------------------------------------------------
bar=(
    Bar()
        .add_xaxis(province_list)
        .add_yaxis("确诊数据", confirm_list)
        .add_yaxis("死亡数据", dead_list)
        .add_yaxis("治愈数据", heal_list)
        .add_yaxis("新增确诊", new_confirm_list)
        .set_global_opts(title_opts=opts.TitleOpts(title="贵州省疫情数据", subtitle="人数"))
    )

bar.render("贵州省疫情2.html")
