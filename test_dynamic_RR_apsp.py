from _graph.GraphPro import GraphPro as g
from time import time
import os

os.system('clear')
print("<--------Test Create------->\n")

num_tries = 10000
sources = [1, 0, 3, 2, 1, 4, 5, 4, 3, 5]
targets = [0, 2, 0, 1, 3, 1, 1, 3, 5, 4]
weights = [2, 2, 4, 3, 2, 4, 4, 3, 5, 1]
graph = g(sources, targets, weights)
graph.print_r()

print("-------Dist FLoyd - Warshall -----")


dist = graph.floyd_warshall()
print(dist)

print("------- Incremental -----")

graph.vertex_update(1, 3, 1)
print(graph.last_vertex_modified)

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


print("------- BFS truncated (each node)-----")

new_dist = graph.bfs_truncated_each_node(dist.tolist())
print(new_dist)
mean_bfs_truncated = 0
for times1 in range(num_tries):
    t = time()
    graph.bfs_truncated_each_node(dist.tolist())
    lapsed = time() - t
    mean_bfs_truncated = mean_bfs_truncated + lapsed
mean_bfs_truncated = mean_bfs_truncated / num_tries
print('Time: ', mean_bfs_truncated)
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
