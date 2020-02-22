# -*- coding: utf-8 -*-
import time, json, requests
import pandas as pd
from pyecharts.charts import Map
import pyecharts.options as opts

#-------------------------------------------------------------------------------------
# 第一步：读取数据
#-------------------------------------------------------------------------------------
n = time.strftime("%Y-%m-%d") + "-china.csv"
data = pd.read_csv(n)
list_data = zip(list(data['province']), list(data['confirm']))
print(list_data)
# [('湖北', 48206), ('广东', 1241), ('河南', 1169), ('浙江', 1145), ..., ('澳门', 10), ('西藏', 1)]


#-------------------------------------------------------------------------------------
# 第二步：绘制全国疫情地图
# 参考文章：https://blog.csdn.net/shineych/article/details/104231072 [shineych大神]
#-------------------------------------------------------------------------------------
def map_cn_disease_dis() -> Map:
    c = (
        Map()
        .add('中国', list_data, 'china')
        .set_global_opts(
            title_opts=opts.TitleOpts(title='全国新型冠状病毒疫情地图（确诊数）'),
            visualmap_opts=opts.VisualMapOpts(is_show=True,
                                              split_number=6,
                                              is_piecewise=True,  # 是否为分段型
                                              pos_top='center',
                                              pieces=[
                                                   {'min': 10000, 'color': '#7f1818'},  #不指定 max
                                                   {'min': 1000, 'max': 10000},
                                                   {'min': 500, 'max': 999},
                                                   {'min': 100, 'max': 499},
                                                   {'min': 10, 'max': 99},
                                                   {'min': 0, 'max': 5} ],                                              
                                              ),
        )
    )
    return c
map_cn_disease_dis().render('全国疫情地图.html')
