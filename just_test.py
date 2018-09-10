from _graph.GraphPro import GraphPro as g
import os

os.system('clear')
print("<--------Test ------->\n")

weights = [1, 2, 3, 4, 5]
graph = g.creategraph(20, .4, weights, directed=False)

graph.print_r()
graph.draw(with_weight=False)





