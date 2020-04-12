# coding=utf-8
import jieba
import re
import time
from collections import Counter
from snownlp import SnowNLP

#------------------------------------中文分词------------------------------------
cut_words = ""
all_words = ""
f = open('all-data-key.txt', 'w', encoding='utf-8')
for line in open('all-data.txt', encoding='utf-8'):
    line = line.strip('\n')
    #停用词过滤
    line = re.sub('[0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~\s]+', "", line)
    seg_list = jieba.cut(line, cut_all=False)
    cut_words = (" ".join(seg_list))

    #计算关键词
    all_words = cut_words.split()
    c = Counter()
    for x in all_words:
        if len(x)>1 and x != '\r\n':
            c[x] += 1
    #Top50
    output = ""
    #print('\n词频统计结果：')
    for (k,v) in c.most_common(50):
        #print("%s:%d"%(k,v))
        output += k + " "
    
    f.write(output+"\n")
else:
    f.close()
