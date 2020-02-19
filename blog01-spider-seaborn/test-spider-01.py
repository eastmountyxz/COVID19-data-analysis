# -*- coding: utf-8 -*-

#------------------------------------------------------------------------------
# 第一步：抓取数据
# 参考文章：许老师博客 https://blog.csdn.net/xufive/article/details/104093197
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
