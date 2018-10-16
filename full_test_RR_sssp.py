from _graph.GraphPro import GraphPro as G
from time import time
import os

#os.system('clear')
print("<--------Test Create------->\n")

num_tries = 1000
sources = [1, 0, 3, 2, 1, 4, 5, 4, 3, 5]
targets = [0, 2, 0, 1, 3, 1, 1, 3, 5, 4]
weights = [2, 2, 4, 3, 2, 4, 4, 3, 5, 1]
graph = G(sources, targets, weights)
graph.print_r()

print("-------Incremental-----")
print("-------Calc source(2)-----")
source = 1
dist = graph.sssp_dijkstra(source)
print(dist)

graph.vertex_update(1, 3, 1)

mean_time_dijkstra_sp = 0
for times1 in range(num_tries):
    t = time()
    graph.sssp_dijkstra(source)
    lapsed = time() - t
    mean_time_dijkstra_sp = mean_time_dijkstra_sp + lapsed
mean_time_dijkstra_sp = mean_time_dijkstra_sp / num_tries

dist_new = graph.dijkstra_truncated(dist.tolist())
print(dist_new)

mean_time_rr_sp = 0
for times2 in range(num_tries):
    t = time()
    graph.dijkstra_truncated(dist.tolist())
    lapsed = time() - t
    mean_time_rr_sp = mean_time_rr_sp + lapsed
mean_time_rr_sp = mean_time_rr_sp / num_tries

print()
print('SSSP Dijkstra: ', mean_time_dijkstra_sp)
print('SSSP RR      :', mean_time_rr_sp)
print('Is less?', mean_time_rr_sp < mean_time_dijkstra_sp)
print()


graph.draw()
print()
print("------------------------")
