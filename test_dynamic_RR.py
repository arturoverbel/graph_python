from _graph.GraphPro import GraphPro as g
import os

os.system('clear')
print("<--------Test Create------->\n")

sources = [1, 2, 3, 2, 1, 4, 5, 4, 3, 5]
targets = [0, 0, 0, 1, 3, 1, 1, 3, 5, 4]
weights = [2, 2, 4, 3, 2, 4, 4, 3, 5, 1]
graph = g(sources, targets, weights)
graph.print_r()

print("-------Incremental-----")
source = 1

dist = graph.sssp_dijkstra(source)
graph.vertex_update(1, 3, 1)

print(dist)
new_dist = graph.dijkstra_truncated(dist)
print(new_dist)

graph.draw()
print()
print("------------------------")
