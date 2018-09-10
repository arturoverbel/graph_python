from _graph.GraphPro import GraphPro as g
from time import time
import os

os.system('clear')
print("<--------Test Dijkstra------->\n")

weights = [1, 2, 3, 4, 5]
graph = g.creategraph(6, .75, weights, directed=False)
graph.print_r()
print('.........................')
t = time()
print(graph.apsp_dijkstra())
elapsed = time() - t
print("Time: ", elapsed)

graph.draw()
