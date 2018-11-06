from _graph.GraphPro import GraphPro as g
import os

os.system('clear')
print("<--------Test Create------->\n")

weights = [1, 2, 3, 4, 5]
graph = g.creategraph(6, .75, weights)
graph.print_r()

print("-------Incremental-----")
data = graph.dynamic_incremental_random_vertex(weights)
graph.print_r()

print("-------Decreasing-----")
data = graph.dynamic_decreasing_random_vertex()
graph.print_r()

print("-------Update Vertex-----")
data = graph.vertex_update_random()
print(data)
graph.print_r()

#graph.draw()
print()
print("------------------------")
