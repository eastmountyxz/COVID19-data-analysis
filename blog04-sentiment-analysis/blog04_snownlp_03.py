# -*- coding: utf-8 -*-
from snownlp import SnowNLP
s1 = SnowNLP(u"我今天很开心")
print(u"s1情感分数:")
print(s1.sentiments)

s2 = SnowNLP(u"我今天很沮丧")
print(u"s2情感分数:")
print(s2.sentiments)

s3 = SnowNLP(u"大傻瓜，你脾气真差，动不动就打人")
print(u"s3情感分数:")
print(s3.sentiments)
