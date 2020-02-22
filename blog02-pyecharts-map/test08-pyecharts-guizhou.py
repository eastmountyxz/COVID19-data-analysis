# -*- coding: utf-8 -*-
import time, json, requests
import pandas as pd
from pyecharts.charts import Map
import pyecharts.options as opts

#-------------------------------------------------------------------------------------
# 第一步：读取数据
#-------------------------------------------------------------------------------------
n = time.strftime("%Y-%m-%d") + "-gz.csv"
data = pd.read_csv(n)
list_data_guizhou = zip(list(data['province']), list(data['confirm']))
gz_data = list(list_data_guizhou)
print(gz_data)

for a,b in gz_data:
    print(a, b, type(b))

#-------------------------------------------------------------------------------------
# 第二步：绘制贵州疫情地图
#-------------------------------------------------------------------------------------
def map_gz_disease_dis() -> Map:
    c = (
        Map()
        .add('贵州省', gz_data, '贵州')
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True, formatter='{b}\n{c}例'))
        .set_global_opts(
                    title_opts=opts.TitleOpts(title='贵州省新型冠状病毒疫情地图（确诊数）'),
                    visualmap_opts=opts.VisualMapOpts(is_show=True,
                                                      split_number=6,
                                                      is_piecewise=True,  # 是否为分段型
                                                      pos_top='center',
                                                      pieces=[
                                                           {'min': 50},  
                                                           {'min': 30, 'max': 49},
                                                           {'min': 20, 'max': 29},
                                                           {'min': 10, 'max': 19},
                                                           {'min': 1, 'max': 9},
                                                           {'value': 0, "label": '无确诊病例', "color": 'green'} ],                                              
                                                      ),
                )
    )
    return c
map_gz_disease_dis().render('贵州省疫情地图.html')
