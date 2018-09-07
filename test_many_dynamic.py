import matplotlib.pyplot as plt
from GraphTest import GraphTest
import os

os.system('clear')
print("<--------Test Create------->\n")

#test = GraphTest(weights=weights)
#print(test.mean(6))

test = GraphTest(num_tries=10)
results = test.node_increments()
plt.plot(results)
plt.show()
