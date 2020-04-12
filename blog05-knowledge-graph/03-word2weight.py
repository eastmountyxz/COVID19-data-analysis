# -*- coding: utf-8 -*-
"""
@author: eastmount CSDN 2020-04-12
"""
import pandas as pd
import numpy as np
import codecs
import networkx as nx
import matplotlib.pyplot as plt
import csv
from scipy.sparse import coo_matrix
 
#---------------------------第一步:读取数据-------------------------------
word = [] #记录关键词
f = open("all-data-key.txt", encoding='utf-8')            
line = f.readline()           
while line:
    #print line
    line = line.replace("\n", "") #过滤换行
    line = line.strip('\n') 
    for n in line.split(' '):
        #print n
        if n not in word:
            word.append(n)
    line = f.readline()
f.close()
print(len(word)) #关键词总数


#--------------------------第二步 计算共现矩阵----------------------------
a = np.zeros([2,3])
print(a)

#共现矩阵
#word_vector = np.zeros([len(word),len(word)], dtype='float16') 

#MemoryError：矩阵过大汇报内存错误
#采用coo_matrix函数解决该问题
print(len(word))
#类型<type 'numpy.ndarray'>
word_vector = coo_matrix((len(word),len(word)), dtype=np.int8).toarray() 
print(word_vector.shape)

f = open("all-data-key.txt", encoding='utf-8')  
line = f.readline()           
while line:
    line = line.replace("\n", "") #过滤换行
    line = line.strip('\n') #过滤换行
    nums = line.split(' ')

    #循环遍历关键词所在位置 设置word_vector计数
    i = 0
    j = 0
    while i<len(nums):         #ABCD共现 AB AC AD BC BD CD加1
        j = i + 1
        w1 = nums[i]           #第一个单词
        while j<len(nums):
            w2 = nums[j]       #第二个单词
            #从word数组中找到单词对应的下标
            k = 0
            n1 = 0
            while k<len(word):
                if w1==word[k]:
                    n1 = k
                    break
                k = k +1
            #寻找第二个关键字位置
            k = 0
            n2 = 0
            while k<len(word):
                if w2==word[k]:
                    n2 = k
                    break
                k = k +1
            #重点: 词频矩阵赋值 只计算上三角
            if n1<=n2:
                word_vector[n1][n2] = word_vector[n1][n2] + 1
            else:
                word_vector[n2][n1] = word_vector[n2][n1] + 1
            #print n1, n2, w1, w2
            j = j + 1
        i = i + 1
    #读取新内容
    line = f.readline()
f.close()


#--------------------------第三步  TXT文件写入--------------------------
res = open("word_word_weight.txt", "a+", encoding='utf-8')
i = 0
while i<len(word):
    w1 = word[i]
    j = 0
    while j<len(word):
        w2 = word[j]
        #判断两个词是否共现 共现&词频不为0的写入文件
        if word_vector[i][j]>0:
            #print w1 +" " + w2 + " "+ str(int(word_vector[i][j]))
            res.write(w1 +" " + w2 + " "+ str(int(word_vector[i][j]))  +  "\n")
        j = j + 1
    i = i + 1
res.close()

#--------------------------第四步  CSV文件写入--------------------------
c = open("word-word-weight.csv","w", encoding='utf-8', newline='')    #解决空行
#c.write(codecs.BOM_UTF8)                                 #防止乱码
writer = csv.writer(c)                                    #写入对象
writer.writerow(['Word1', 'Word2', 'Weight'])

i = 0
while i<len(word):
    w1 = word[i]
    j = 0 
    while j<len(word):
        w2 = word[j]
        #判断两个词是否共现 共现词频不为0的写入文件
        if word_vector[i][j]>0:
            #写入文件
            templist = []
            templist.append(w1)
            templist.append(w2)
            templist.append(str(int(word_vector[i][j])))
            #print templist
            writer.writerow(templist)
        j = j + 1
    i = i + 1
c.close()
