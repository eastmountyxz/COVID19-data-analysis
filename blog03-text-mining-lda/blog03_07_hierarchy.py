# -*- coding: utf-8 -*-
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import jieba
import matplotlib.pyplot as plt
from pylab import mpl
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity
from scipy.cluster.hierarchy import ward, dendrogram
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

mpl.rcParams['font.sans-serif'] = ['SimHei']

#------------------------------ 第一步 计算TOP100 ------------------------------
# 计算中文分词词频TOP100
cut_words = ""
all_words = ""
for line in open('C-class.txt', encoding='utf-8'):
    line.strip('\n')
    seg_list = jieba.cut(line,cut_all=False)
    # print(" ".join(seg_list))
    cut_words = (" ".join(seg_list))
    all_words += cut_words
    
# 输出结果
all_words = all_words.split()
print(all_words)

# 词频统计
c = Counter()
for x in all_words:
    if len(x)>1 and x != '\r\n':
        c[x] += 1

# 输出词频最高的前10个词
top_word = []
print('\n词频统计结果：')
for (k,v) in c.most_common(100):
    print("%s:%d"%(k,v))
    top_word.append(k)
print(top_word)
# ['疫情', '防控', '组织', '工作'...]

#------------------------------ 第二步 中文分词过滤 ------------------------------
# 过滤
cut_words = ""
f = open('C-key.txt', 'w')
for line in open('C-class.txt', encoding='utf-8'):
    line.strip('\n')
    seg_list = jieba.cut(line,cut_all=False)
    final = ""
    for seg in seg_list:
        if seg in top_word:
            final += seg + "|"
    cut_words += final
    f.write(final+"\n")
print(cut_words)
f.close

#------------------------------ 第三步 相相关计算 ------------------------------ 
text = open('C-key.txt').read()
list1 = text.split("\n")
print(list1)

# 数据第一行、第二行数据
# print(list1[0])
# print(list1[1])
mytext_list = list1

# min_df用于删除不经常出现的术语
# max_df用于删除过于频繁出现的术语,也称为语料库特定的停用词
# count_vec = CountVectorizer(min_df=3, max_df=3)
count_vec = CountVectorizer(min_df=3)
xx1 = count_vec.fit_transform(list1).toarray()
word = count_vec.get_feature_names() 
print("word feature length: {}".format(len(word)))
print(word)
print(xx1.shape)
print(xx1[0])
titles = word

#------------------------------ 第四步 相似度计算 ------------------------------ 
df = pd.DataFrame(xx1)
print(df.corr())
print(df.corr('spearman'))
print(df.corr('kendall'))

dist = df.corr()
print(dist)
print(type(dist))
print(dist.shape)

#------------------------------ 第五步 可视化分析 ------------------------------ 
# define the linkage_matrix using ward clustering pre-computed distances
linkage_matrix = ward(dist)
fig, ax = plt.subplots(figsize=(15, 20)) # set size
ax = dendrogram(linkage_matrix, orientation="right", labels=titles);

# how plot with tight layout
plt.tight_layout() 

# save figure as ward_clusters
plt.savefig('Tree_word.png', dpi=200) 
