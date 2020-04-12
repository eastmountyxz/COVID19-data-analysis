# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
 
#定义有向图
DG = nx.Graph() 
#添加五个节点(列表)
DG.add_nodes_from(['A', 'B', 'C', 'D'])
print(DG.nodes())
#添加边(列表)
DG.add_edge('A', 'B', weight=1)
DG.add_edge('A', 'C', weight=2)
DG.add_edge('A', 'D', weight=1)
DG.add_edge('B', 'C', weight=1)
DG.add_edge('B', 'D', weight=1)
DG.add_edge('C', 'D', weight=1)
#DG.add_edges_from([('A', 'B'), ('A', 'C'), ('A', 'D'), ('B','C'),('B','D'),('C','D')])
print(DG.edges())
#绘制图形 设置节点名显示\节点大小\节点颜色
colors = ['red', 'green', 'blue', 'yellow']
nx.draw(DG,with_labels=True, node_size=900, node_color = colors)
plt.show()
