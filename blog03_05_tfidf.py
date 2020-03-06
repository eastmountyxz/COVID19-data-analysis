# coding=utf-8 
import os
import time
import pandas as pd
import numpy as np
import jieba
import jieba.analyse
import matplotlib.pyplot as plt
from PIL import Image
from datetime import datetime
from matplotlib.font_manager import FontProperties

#------------------------------------中文分词------------------------------------
cut_words = ""
for line in open('C-class.txt', encoding='utf-8'):
    line.strip('\n')
    seg_list = jieba.cut(line,cut_all=False)
    # print(" ".join(seg_list))
    cut_words += (" ".join(seg_list))

# jieba.load_userdict("userdict.txt")              # 自定义词典
# jieba.analyse.set_stop_words('stop_words.txt')   # 停用词词典

# 提取主题词 返回的词频其实就是TF-IDF
keywords = jieba.analyse.extract_tags(cut_words,
                                      topK=50,
                                      withWeight=True,
                                      allowPOS=('a','e','n','nr','ns', 'v')) #词性 形容词 叹词 名词 动词

# 以列表形式返回
print(keywords)

# 数据存储
pd.DataFrame(keywords, columns=['词语','重要性']).to_excel('TF_IDF关键词前50.xlsx')

# keyword本身包含两列数据
ss = pd.DataFrame(keywords,columns = ['词语','重要性'])     
# print(ss)

#------------------------------------数据可视化------------------------------------
plt.figure(figsize=(10,6))
plt.title('TF-IDF Ranking')
fig = plt.axes()
plt.barh(range(len(ss.重要性[:25][::-1])),ss.重要性[:25][::-1])
fig.set_yticks(np.arange(len(ss.重要性[:25][::-1])))
font = FontProperties(fname=r'c:\windows\fonts\simsun.ttc')
fig.set_yticklabels(ss.词语[:25][::-1],fontproperties=font)
fig.set_xlabel('Importance')
plt.show()
     


