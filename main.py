import graph_pro as g
import os

os.system('cls')
print("<------------------------>")
print("Main\n")

source = [1,2,2,2,3,4,2,5]
target = [2,1,3,4,4,3,5,4]
weight = [1,1,2,4,1,1,2,2]

G = g.graph_pro(source, target, weight)
G.print()

print("------------------------")
print("Dikstra: ")
print(G.dijkstra(1))