from graphviz import Digraph,Graph
import numpy.random as npr

# formatはpngを指定(他にはPDF, PNG, SVGなどが指定可)
# G = Digraph(format='png',engine="fdp")
G = Digraph(format='png',engine="circo")
G.attr('node', shape='circle')
G.attr(overlap='false')

# ノードの追加
name = "arayama"
for i in name:
    G.node(i, i)

# 辺の追加
for i in range(1,len(name)):
    G.edge(name[i-1],name[i])

# print()するとdot形式で出力される
print(G)

# binary_tree.pngで保存
G.render('graph1')


