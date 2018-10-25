from _graph.GraphPro import GraphPro as g
from time import time
import os

os.system('clear')
print("<--------Test Khopkar------->\n")

weights = [1, 2, 3, 4, 5]

sources = [1, 0, 3, 2, 1, 4, 5, 4, 5]
targets = [0, 2, 0, 1, 3, 1, 1, 3, 4]
weights = [2, 2, 4, 3, 2, 4, 4, 3, 1]
graph = g(sources, targets, weights)

print('.........................')

dist = graph.floyd_warshall()
print(dist)

graph.dynamic_incremental_node(
    node=6, sources=[2], w_sources=[1], targets=[5], w_targets=[1])

dist_new = graph.knnb_node_incremental(dist.tolist())
print(dist_new)

graph.print_r()
#graph.draw()


sources = [10, 11, 5, 5, 6, 4, 8, 4, 9, 9,  2, 12, 3]
targets = [1,   1, 1, 6, 4, 7, 4, 9, 8, 2, 12,  9, 2]
weights = [1,   1, 1, 1, 1, 1, 1, 1, 1, 1,  1,  1, 1]
graph2 = g(sources, targets, weights)

print('.........................')

dist2 = graph2.floyd_warshall()
print(dist2)

graph2.dynamic_incremental_node(
    node=13, sources=[1, 3], w_sources=[1, 1], targets=[2, 4], w_targets=[1, 1])

dist2_new = graph2.knnb_node_incremental(dist2.tolist())
print(dist2_new)

graph2.print_r()


