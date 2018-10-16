from _graph.GraphPro import GraphPro as g
from time import time
import os

os.system('clear')
print("<--------Test Create------->\n")

num_tries = 10
weights = [1, 2, 3, 4, 5]
graph = g.creategraph(6, .9, weights)
graph.print_r()

dist = graph.floyd_warshall()
print(dist)

print("-------Incremental-----")
graph.vertex_update_random()

print("------- Floyd -Warshall after Update -----")

dist_fw = graph.floyd_warshall()
print(dist_fw)
mean_time_fw = 0
for times1 in range(num_tries):
    t = time()
    graph.floyd_warshall()
    lapsed = time() - t
    mean_time_fw = mean_time_fw + lapsed
mean_time_fw = mean_time_fw / num_tries
print('Time: ', mean_time_fw)

print("------- BFS truncated (only source affected)-----")

source_affected = graph.find_source_affected(dist.tolist())
print(source_affected)

dist_rr = graph.bfs_truncated_with_sources(dist.tolist())
print(dist_rr)
mean_bfs_truncated_only_sources = 0
for times1 in range(num_tries):
    t = time()
    graph.bfs_truncated_with_sources(dist.tolist())
    lapsed = time() - t
    mean_bfs_truncated_only_sources = mean_bfs_truncated_only_sources + lapsed
mean_bfs_truncated_only_sources = mean_bfs_truncated_only_sources / num_tries
print('Time: ', mean_bfs_truncated_only_sources)

#graph.draw()
print()
print("------------------------")
