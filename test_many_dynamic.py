import matplotlib.pyplot as plt
from GraphTest import GraphTest
import numpy as np
import os

os.system('clear')
print("<--------Test ------->\n")

#test = GraphTest(weights=weights)
#print(test.mean(6))

test = GraphTest(num_tries=1000)
results = test.node_increments()

num_nodes = np.arange(test.from_num_nodes, test.until_num_nodes, 1)
plt.plot(num_nodes, results,'ro')
plt.ylabel('Tiempo en promedio para resolver')
plt.xlabel('Número de nodos')
plt.show()
