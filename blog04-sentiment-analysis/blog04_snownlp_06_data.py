# -*- coding: utf-8 -*-
from snownlp import SnowNLP
import codecs
import os

#获取情感分数
source = open("data.txt","r", encoding='utf-8')
line = source.readlines()
sentimentslist = []
for i in line:
    s = SnowNLP(i)
    print(s.sentiments)
    sentimentslist.append(s.sentiments)

#区间转换为[-0.5, 0.5]
result = []
i = 0
while i<len(sentimentslist):
    result.append(sentimentslist[i]-0.5)
    i = i + 1

#可视化画图
import matplotlib.pyplot as plt
import numpy as np
plt.plot(np.arange(0, 356, 1), result, 'k-')
plt.xlabel('Number')
plt.ylabel('Sentiment')
plt.title('Analysis of Sentiments')
plt.show()
