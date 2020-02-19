# -*- coding: utf-8 -*-
# 参考文章：许老师博客 https://blog.csdn.net/xufive/article/details/104093197
import time, json, requests
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 抓取腾讯疫情实时json数据
def catch_daily():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=wuwei_ww_cn_day_counts&callback=&_=%d'%int(time.time()*1000)
    data = json.loads(requests.get(url=url).json()['data'])
    data.sort(key=lambda x:x['date'])
    
    date_list = list() # 日期
    confirm_list = list() # 确诊
    suspect_list = list() # 疑似
    dead_list = list() # 死亡
    heal_list = list() # 治愈
    for item in data:
        month, day = item['date'].split('/')
        date_list.append(datetime.strptime('2020-%s-%s'%(month, day), '%Y-%m-%d'))
        confirm_list.append(int(item['confirm']))
        suspect_list.append(int(item['suspect']))
        dead_list.append(int(item['dead']))
        heal_list.append(int(item['heal']))
    return date_list, confirm_list, suspect_list, dead_list, heal_list

# 绘制每日确诊和死亡数据
def plot_daily():
    
    
    date_list, confirm_list, suspect_list, dead_list, heal_list = catch_daily() # 获取数据
    
    plt.figure('2019-nCoV疫情统计图表', facecolor='#f4f4f4', figsize=(10, 8))
    plt.title('2019-nCoV疫情曲线', fontsize=20)

    plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False    #用来正常显示负号

    plt.plot(date_list, confirm_list, 'r-', label='确诊')
    plt.plot(date_list, confirm_list, 'rs')
    plt.plot(date_list, suspect_list, 'b-',label='疑似')
    plt.plot(date_list, suspect_list, 'b*')
    plt.plot(date_list, dead_list, 'y-', label='死亡')
    plt.plot(date_list, dead_list, 'y+')
    plt.plot(date_list, heal_list, 'g-', label='治愈')
    plt.plot(date_list, heal_list, 'gd')
    
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d')) # 格式化时间轴标注
    plt.gcf().autofmt_xdate() # 优化标注（自动倾斜）
    plt.grid(linestyle=':') # 显示网格
    plt.legend(loc='best') # 显示图例
    plt.savefig('2019-nCoV疫情曲线.png') # 保存为文件
    plt.show()

if __name__ == '__main__':
    plot_daily()
