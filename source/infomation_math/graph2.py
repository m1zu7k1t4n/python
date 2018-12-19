from graphviz import Digraph,Graph
import numpy.random as npr

# formatはpngを指定(他にはPDF, PNG, SVGなどが指定可)
# G = Digraph(format='png',engine="fdp")
G = Digraph(format='png',engine="neato")
G.attr('node', shape='circle')
G.attr(overlap='false')


# ノードの追加
name = ["海","川","工場","家庭","下水道","ポンプ場","最初沈砂池","生物反応槽","最終沈砂池","汚泥処理場","廃棄場"]
for i in name:
    G.node(i, i)

# 辺の追加
G.edge("海","川")
G.edge("工場","下水道")
G.edge("家庭","下水道")
G.edge("下水道","ポンプ場")
G.edge("ポンプ場","最初沈砂池")
G.edge("最初沈砂池","生物反応槽")
G.edge("生物反応槽","最終沈砂池")
G.edge("最初沈砂池","汚泥処理場")
G.edge("最終沈砂池","汚泥処理場")
G.edge("汚泥処理場","廃棄場")
G.edge("最終沈砂池","生物反応槽")
G.edge("最終沈砂池","川")

# print()するとdot形式で出力される
print(G)

# binary_tree.pngで保存
G.render('graph2')

