from _graph.GraphPro import GraphPro as g
import os

os.system('clear')
print("<--------Test Create------->\n")

sources = [0, 1, 0, 2, 3, 1, 2, 1, 3, 1, 4, 1, 5, 3, 4, 3, 5, 4, 5]
targets = [1, 0, 2, 0, 0, 2, 1, 3, 1, 4, 1, 5, 1, 4, 3, 5, 3, 5, 4]
weights = [2, 2, 2, 2, 4, 3, 3, 2, 2, 4, 4, 4, 4, 3, 3, 5, 5, 1, 1]
graph = g(sources, targets, weights)
graph.print_r()

print("-------Incremental-----")
source = 2

dist = graph.floyd_warshall()
graph.vertex_update(1, 3, 1)

print(dist)
new_dist = graph.apsp_dijkstra_truncated(0, dist)
print(new_dist)

graph.draw()
print()
print("------------------------")
