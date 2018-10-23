from _graph.GraphPro import GraphPro as g
from time import time
import os

os.system('clear')
print("<--------Test Floyd-Warshall------->\n")

weights = [1, 2, 3, 4, 5]
#graph = g.creategraph(6, .75, weights, directed=False)
sources = [1, 0, 3, 2, 1, 4, 5, 4, 5]
targets = [0, 2, 0, 1, 3, 1, 1, 3, 4]
weights = [2, 2, 4, 3, 2, 4, 4, 3, 1]
graph = g(sources, targets, weights)

print('.........................')

dist = graph.floyd_warshall()
print(dist)

graph.dynamic_incremental_vertex(3, 5, 5)

dist_new = graph.kk_incremental(dist.tolist())

graph.draw()
