# coding=utf-8
import jieba
import re
import sys
import time
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#------------------------------------中文分词------------------------------------
cut_words = ""
all_words = ""
f = open('data-fenci.txt', 'w')
for line in open('data.txt', encoding='utf-8'):
    line.strip('\n')
    seg_list = jieba.cut(line,cut_all=False)
    # print(" ".join(seg_list))
    cut_words = (" ".join(seg_list))
    f.write(cut_words)
    all_words += cut_words
else:
    f.close()

# 输出结果
all_words = all_words.split()
print(all_words)

# 词频统计
c = Counter()
for x in all_words:
    if len(x)>1 and x != '\r\n':
        c[x] += 1

# 输出词频最高的前10个词
print('\n词频统计结果：')
for (k,v) in c.most_common(10):
    print("%s:%d"%(k,v))

# 存储数据
name = time.strftime("%Y-%m-%d") + "-fc.csv"
fw = open(name, 'w', encoding='utf-8')
i = 1
for (k,v) in c.most_common(len(c)):
    fw.write(str(i)+','+str(k)+','+str(v)+'\n')
    i = i + 1
else:
    print("Over write file!")
    fw.close()

#------------------------------------词云分析------------------------------------
#打开本体TXT文件
text = open('data.txt').read()
 
#结巴分词 cut_all=True 设置为精准模式 
wordlist = jieba.cut(text, cut_all = False)
 
#使用空格连接 进行中文分词
wl_space_split = " ".join(wordlist)
#print(wl_space_split)
 
#对分词后的文本生成词云
my_wordcloud = WordCloud().generate(wl_space_split)
 
#显示词云图
plt.imshow(my_wordcloud)
#是否显示x轴、y轴下标
plt.axis("off")
plt.show()
