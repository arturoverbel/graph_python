import numpy as np
import graphpro as g
import os

os.system('clear')
print("<------------------------>")
print("Test\n")

repeticiones = 1000
datas = [0, 1, 2]
probabilities = [0.4, 0.5, 0.1]
results = np.zeros(repeticiones)

for n in range(repeticiones):
    results[n] = g.GraphPro.probability(datas, probabilities)

total = len(datas)
fr = np.zeros(total)

for n in range(total):
    fr[n] = np.sum(results == datas[n]) / repeticiones

print(fr)

print("------------------------")