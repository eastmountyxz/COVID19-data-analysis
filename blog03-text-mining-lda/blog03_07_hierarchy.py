# -*- coding: utf-8 -*-
import os
import codecs
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import jieba
from sklearn import metrics
from sklearn.metrics import silhouette_score
from array import array
from numpy import *

from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']

#------------------------------ 第一步 加载语料 ------------------------------ 
text = open('C-class-fenci.txt', "r", encoding='UTF-8').read()
print(type(text))
print(text)

list1 = text.split("\n")
print(list1)
print(list1[0])
print(list1[1])
mytext_list = list1

count_vec = CountVectorizer(min_df=3, max_df=3)
xx1 = count_vec.fit_transform(list1).toarray()
word = count_vec.get_feature_names() 
print("word feature length: {}".format(len(word)))
print(word)
print(xx1)
print(type(xx1))

print(xx1.shape)
print(xx1[0])
titles = word

#------------------------------ 第二步 相似度计算 ------------------------------ 
from sklearn.metrics.pairwise import cosine_similarity
df = pd.DataFrame(xx1)
print(df.corr())
print(df.corr('spearman'))
print(df.corr('kendall'))

dist = df.corr()
print(dist)
print(type(dist))
print(dist.shape)

#------------------------------ 第三步 可视化分析 ------------------------------ 
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.cluster.hierarchy import ward, dendrogram

#define the linkage_matrix using ward clustering pre-computed distances
linkage_matrix = ward(dist)
fig, ax = plt.subplots(figsize=(15, 20)) # set size
ax = dendrogram(linkage_matrix, orientation="right", labels=titles);

#s how plot with tight layout
plt.tight_layout() 

# save figure as ward_clusters
plt.savefig('KH.png', dpi=200) 
