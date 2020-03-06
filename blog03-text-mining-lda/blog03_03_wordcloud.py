# coding=utf-8
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType

# 数据
words = [
    ('背包问题', 10000),
    ('大整数', 6181),
    ('Karatsuba乘法算法', 4386),
    ('穷举搜索', 4055),
    ('傅里叶变换', 2467),
    ('状态树遍历', 2244),
    ('剪枝', 1868),
    ('Gale-shapley', 1484),
    ('最大匹配与匈牙利算法', 1112),
    ('线索模型', 865),
    ('关键路径算法', 847),
    ('最小二乘法曲线拟合', 582),
    ('二分逼近法', 555),
    ('牛顿迭代法', 550),
    ('Bresenham算法', 462),
    ('粒子群优化', 366),
    ('Dijkstra', 360),
    ('A*算法', 282),
    ('负极大极搜索算法', 273),
    ('估值函数', 265)
]

# 渲染图
def wordcloud_base() -> WordCloud:
    c = (
        WordCloud()
        .add("", words, word_size_range=[20, 100], shape='diamond')  # SymbolType.ROUND_RECT
        .set_global_opts(title_opts=opts.TitleOpts(title='WordCloud词云'))
    )
    return c

# 生成图
wordcloud_base().render('词云图.html')

