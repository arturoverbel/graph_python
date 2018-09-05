import graphpro as g
import os

os.system('clear')
print("<--------Test Create------->\n")

weights = [1, 2, 3, 4, 5]
graph = g.GraphPro.creategraph(5, .4, weights)
graph.print_r()

print("-------Incremental-----")
data = graph.dynamic_incremental_random_vertex(weights)
print(data)
graph.print_r()
print("--------Decreasing-------")
data = graph.dynamic_decreasing_random_vertex()
print(data)
graph.print_r()

print("------------------------")