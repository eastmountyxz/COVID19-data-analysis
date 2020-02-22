# -*- coding: utf-8 -*-
# By: Eastmount CSDN xiuzhang
import time, json, requests
from datetime import datetime
import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.commons.utils import JsCode

#-------------------------------------------------------------------------------------
# 第一步：读取数据
#-------------------------------------------------------------------------------------
n = time.strftime("%Y-%m-%d") + "-daily.csv"
data = pd.read_csv(n)
date_list = list(data['date'])
confirm_list = list(data['confirm'])
suspect_list = list(data['suspect'])
dead_list = list(data['dead'])
heal_list = list(data['heal'])
print(date_list)                        # 日期
print(confirm_list)                     # 确诊数据
print(suspect_list)                     # 疑似数据
print(dead_list)                        # 死亡数据
print(heal_list)                        # 治愈数据


#-------------------------------------------------------------------------------------
# 第二步：绘制柱状图
#-------------------------------------------------------------------------------------
line = (
    Line()
    .add_xaxis(date_list)
    .add_yaxis('确诊数据', confirm_list)
    .add_yaxis('疑似数据', suspect_list, is_smooth=True) #平滑
    .add_yaxis('死亡数据', dead_list)
    .add_yaxis('治愈数据', heal_list)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    # 设置x轴标签旋转角度
    .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30)), 
                     yaxis_opts=opts.AxisOpts(name='人数', min_=3), 
                     title_opts=opts.TitleOpts(title='2019-nCoV疫情曲线图'))        
    )

line.render('2019-nCoV疫情曲线图.html')
