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

# 获取贵州下标
k = 0
for item in num:
    print(item['name'],end=" ")   # 不换行
    if item['name'] in "贵州":
        print("")
        print(item['name'], k)
        break
    k = k + 1
print("") # 换行

# 显示贵州省数据
gz = num[k]['children']
for item in gz:
    print(item)
else:
    print("\n")
