# coding=utf-8
import jieba
import re
import time
from collections import Counter

#------------------------------------中文分词------------------------------------
cut_words = ""
all_words = ""
f = open('C-class-fenci.txt', 'w')
for line in open('C-class.txt', encoding='utf-8'):
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
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType

# 生成数据 word = [('A',10), ('B',9), ('C',8)] 列表+Tuple
words = []
for (k,v) in c.most_common(1000):
    # print(k, v)
    words.append((k,v))

# 渲染图
def wordcloud_base() -> WordCloud:
    c = (
        WordCloud()
        .add("", words, word_size_range=[20, 100], shape=SymbolType.ROUND_RECT)
        .set_global_opts(title_opts=opts.TitleOpts(title='全国新型冠状病毒疫情词云图'))
    )
    return c

# 生成图
wordcloud_base().render('疫情词云图.html')
