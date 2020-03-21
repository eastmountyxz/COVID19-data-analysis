# -*- coding: utf-8 -*-
from snownlp import SnowNLP
s = SnowNLP(u"这本书质量真不太好！")

print(u"\n中文分词:")
print( " ".join(s.words))

print(u"\n词性标注:")
print(s.tags)
for k in s.tags:
    print(k)

print(u"\n情感分数:")
print(s.sentiments)

print(u"\n转换拼音:")
print(s.pinyin)

print(u"\n输出前4个关键词:")
print(s.keywords(4))
for k in s.keywords(4):
    print(k)

print(u"\n输出关键句子:")
print(s.summary(1))
for k in s.summary(1):
    print(k)

print(u"\n输出tf和idf:")
print(s.tf)
print(s.idf)

n = SnowNLP(u'「繁體字」「繁體中文」的叫法在臺灣亦很常見。')
print(u"\n繁简体转换:")
print(n.han)
