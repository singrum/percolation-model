# nx로 격자 그래프 생성
import networkx as nx
import matplotlib.pyplot as plt
# 5x5 격자 그래프 생성
G = nx.grid_2d_graph(100,100)

# 각 엣지에 0~1 랜덤 할당
import random
for (u, v) in G.edges():
    G.edges[u, v]['weight'] = random.random()


