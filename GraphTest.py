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
        mean_dijkstra = 0
        mean_floyd = 0
        if self.num_tries <= 0:
            return 0
        for times in range(self.num_tries):
            graph = g.creategraph(num_nodes, self.probability_edges, self.weights)

            t = time()
            graph.apsp_dijkstra()
            lapsed = time() - t
            mean_dijkstra = mean_dijkstra + lapsed

            t = time()
            graph.floyd_warshall()
            lapsed = time() - t
            mean_floyd = mean_floyd + lapsed

        return [mean_dijkstra / self.num_tries, mean_floyd / self.num_tries]

    def node_increments(self):

        num_nodes = self.from_num_nodes
        num_tries = self.until_num_nodes-self.from_num_nodes
        results = np.zeros((2, num_tries))

        for x in range(num_tries):
            print('Size nodes: ', num_nodes)

            times = self.mean(num_nodes)
            results[0, x] = times[0]
            results[1, x] = times[1]
            num_nodes = num_nodes + 1

        return results

    def mean_dynamic(self, num_nodes):
        mean_1 = 0
        mean_2 = 0
        if self.num_tries <= 0:
            return 0
        for times in range(self.num_tries):
            graph = g.creategraph(num_nodes, self.probability_edges, self.weights)
            dist = graph.floyd_warshall()
            graph.vertex_update_random()

            t = time()
            graph.floyd_warshall()
            lapsed = time() - t
            mean_1 = mean_1 + lapsed

            t = time()
            graph.bfs_truncated_with_sources(dist.tolist())
            lapsed = time() - t
            mean_2 = mean_2 + lapsed

        return [mean_1 / self.num_tries, mean_2 / self.num_tries]

    def node_increments_dynamic(self):

        num_nodes = self.from_num_nodes
        num_tries = self.until_num_nodes-self.from_num_nodes
        results = np.zeros((2, num_tries))

        for x in range(num_tries):
            print('Size nodes: ', num_nodes)

            times = self.mean_dynamic(num_nodes)
            results[0, x] = times[0]
            results[1, x] = times[1]
            num_nodes = num_nodes + 1

        return results


