import matplotlib.pyplot as plt
import networkx as nx
import graph as g
import os

os.system('cls')
print("Test Dijkstra\n")

source = [1,2,2,3]
target = [2,3,4,4]
weight = [1,2,4,1]

G = g.graph()
G.network(source, target, weight)

G.dijkstra()


G.print_distances()
