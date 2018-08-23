import numpy as np
import graphpro as g
import os
import networkx as nx
import matplotlib.pyplot as plt

os.system('clear')
print("<------------------------>")
print("Test Create\n")

graph = g.GraphPro.creategraph(5, .65, [1, 2, 3, 4, 5])
graph.print_r()

print("------------------------")
data = graph.set_dynamic_vertex('decreasing')
print(data)
graph.print_r()

print("------------------------")