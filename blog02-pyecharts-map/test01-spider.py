# -*- coding: utf-8 -*-
import time, json, requests
from datetime import datetime

#------------------------------------------------------------------------------
# 第一步 抓取腾讯疫情实时json数据
# 参考文章：许老师博客 https://blog.csdn.net/xufive/article/details/104093197
#------------------------------------------------------------------------------
def catch_daily():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=wuwei_ww_cn_day_counts&callback=&_=%d'%int(time.time()*1000)
    data = json.loads(requests.get(url=url).json()['data'])
    data.sort(key=lambda x:x['date'])
    
    date_list = list()        # 日期
    confirm_list = list()     # 确诊
    suspect_list = list()     # 疑似
    dead_list = list()        # 死亡
    heal_list = list()        # 治愈
    for item in data:
        month, day = item['date'].split('/')
        date_list.append(datetime.strptime('2020-%s-%s'%(month, day), '%Y-%m-%d'))
        confirm_list.append(int(item['confirm']))
        suspect_list.append(int(item['suspect']))
        dead_list.append(int(item['dead']))
        heal_list.append(int(item['heal']))
    return date_list, confirm_list, suspect_list, dead_list, heal_list


#------------------------------------------------------------------------------
# 第二步 存储数据至CSV文件
#------------------------------------------------------------------------------
def load_csv():
    # 获取数据
    date_list, confirm_list, suspect_list, dead_list, heal_list = catch_daily()
    print(date_list)                        # 日期
    print(confirm_list)                     # 确诊数据
    print(suspect_list)                     # 疑似数据
    print(dead_list)                        # 死亡数据
    print(heal_list)                        # 治愈数据

    # 获取当前日期命名(2020-02-13-daily.csv)
    n = time.strftime("%Y-%m-%d") + "-daily.csv"
    fw = open(n, 'w', encoding='utf-8')
    fw.write('date,confirm,suspect,dead,heal\n')
    i = 0
    while i<len(date_list):
        date = str(date_list[i].strftime("%Y-%m-%d"))
        fw.write(date+','+str(confirm_list[i])+','+str(suspect_list[i])+','+str(dead_list[i])+','+str(heal_list[i])+'\n')
        i = i + 1
    else:
        print("Over write file!")
        fw.close()

# 主函数
if __name__ == '__main__':
    load_csv()
