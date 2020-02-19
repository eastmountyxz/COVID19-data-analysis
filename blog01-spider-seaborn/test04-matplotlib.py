# -*- coding: utf-8 -*-

#------------------------------------------------------------------------------
# 第一步：抓取数据
#------------------------------------------------------------------------------
import time, json, requests
# 抓取腾讯疫情实时json数据
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d'%int(time.time()*1000)
data = json.loads(requests.get(url=url).json()['data'])
print(data)
print(data.keys())

# 统计省份信息(34个省份 湖北 广东 河南 浙江 湖南 安徽....)
num = data['areaTree'][0]['children']
print(len(num))
for item in num:
    print(item['name'],end=" ")   # 不换行
else:
    print("\n")                     # 换行
    
# 显示湖北省数据
hubei = num[0]['children']
for item in hubei:
    print(item)
else:
    print("\n")

# 解析数据(确诊 疑似 死亡 治愈)
total_data = {}
for item in num:
    if item['name'] not in total_data:
        total_data.update({item['name']:0})
    for city_data in item['children']:
        total_data[item['name']] +=int(city_data['total']['confirm'])    
print(total_data)
# {'湖北': 48206, '广东': 1241, '河南': 1169, '浙江': 1145, '湖南': 968, ...,  '澳门': 10, '西藏': 1}

#------------------------------------------------------------------------------
# 第二步：绘制柱状图
#------------------------------------------------------------------------------
import matplotlib.pyplot as plt 
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    #用来正常显示负号

#获取数据
names = total_data.keys()
nums = total_data.values()
print(names)
print(nums)

# 绘图
plt.figure(figsize=[10,6])
plt.bar(names, nums, width=0.3, color='green')

# 设置标题
plt.xlabel("地区", fontproperties='SimHei', size=12)
plt.ylabel("人数", fontproperties='SimHei', rotation=90, size=12)
plt.title("全国疫情确诊数对比图", fontproperties='SimHei', size=16)
plt.xticks(list(names), fontproperties='SimHei', rotation=-45, size=10)
# 显示数字
for a, b in zip(list(names), list(nums)):
    plt.text(a, b, b, ha='center', va='bottom', size=6)
plt.show()
