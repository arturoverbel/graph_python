import matplotlib.pyplot as plt
from GraphTest import GraphTest
import numpy as np
import os

os.system('clear')
print("<--------Test ------->\n")

test = GraphTest(num_tries=1000)
results = test.node_increments()
num_nodes = np.arange(test.from_num_nodes, test.until_num_nodes, 1)

np.savetxt('test_algoritms_apsp.out', (num_nodes, results[0], results[1]))

plt.plot(num_nodes, results[0], 'ro', num_nodes, results[1], 'r--')
plt.ylabel('Tiempo en promedio para resolver')
plt.xlabel('Número de nodos')
plt.show()
