import matplotlib.pyplot as plt
import networkx as nx
import graph as g
import os

os.system('cls')
print("Test Dijkstra\n")

source = [1,2,2,2,3,4]
target = [2,1,3,4,4,3]
weight = [1,1,2,4,1,1]

G = g.graph()
G.create_network(source, target, weight)

G.dijkstra()
G.print_distances()

G.floyd_warshall()
G.print_distances()

nx.draw( G.getGraph() )
plt.show()