from _graph.GraphPro import GraphPro as g
from time import time
import os

os.system('clear')
print("<--------Test Create------->\n")

weights = [1, 2, 3, 4, 5]
graph = g.creategraph(5, .4, weights)
graph.print_r()
t = time()
print(graph.apsp_dijkstra())
elapsed = time() - t
print("Time: ", elapsed)

print()
print("-------Incremental-----")
data = graph.dynamic_incremental_random_vertex(weights)
graph.print_r()
t = time()
print(graph.apsp_dijkstra())
elapsed = time() - t
print("Time: ", elapsed)

print()
print("--------Decreasing-------")
data = graph.dynamic_decreasing_random_vertex()
graph.print_r()
t = time()
print(graph.apsp_dijkstra())
elapsed = time() - t
print("Time: ", elapsed)

print()
print("------------------------")