from _graph.GraphPro import GraphPro as g
from time import time
import numpy as np


class GraphTest:

    def __init__(self, from_num_nodes=5, until_num_nodes=20, probability_edges=.5, num_tries=3000, weights=[1, 2, 3, 4, 5, 6]):
        self.from_num_nodes = from_num_nodes
        self.until_num_nodes = until_num_nodes
        self.probability_edges = probability_edges
        self.num_tries = num_tries
        self.weights = weights

    def mean(self, num_nodes):
        mean = 0
        if self.num_tries <= 0:
            return 0
        for times in range(self.num_tries):
            graph = g.creategraph(num_nodes, self.probability_edges, self.weights)
            t = time()
            graph.apsp_dijkstra()
            lapsed = time() - t
            mean = mean + lapsed
        return mean / self.num_tries

    def node_increments(self):

        num_nodes = self.from_num_nodes
        num_tries = self.until_num_nodes-self.from_num_nodes
        results = np.zeros(num_tries)

        for x in range(num_tries):
            results[x] = self.mean(num_nodes)
            num_nodes = num_nodes + 1

        return results


