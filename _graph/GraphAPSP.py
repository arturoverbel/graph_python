import numpy as np
from _graph.DynamicGraph import DynamicGraph


class GraphAPSP(DynamicGraph):

    def __init__(self, source=[], target=[], weight=[]):
        DynamicGraph.__init__(self, source, target, weight)

    def sssp_dijkstra(self, source):

        total_vertex = len(self.vertex)
        Q = np.array(self.vertex)

        dist = np.zeros(total_vertex)
        dist.fill(np.inf)

        dist[self.vertex == source] = 0

        while len(Q) != 0:

            min = np.inf
            u = 0
            for q in Q:
                if dist[self.vertex == q] <= min:
                    min = dist[self.vertex == q]
                    u = q

            Q = np.delete(Q, np.argwhere(Q == u))

            for v in self.target[self.source == u]:
                alt = dist[self.vertex == u] + self.get_weight(u, v)
                index_v = self.vertex == v
                if alt < dist[index_v]:
                    dist[index_v] = alt

        return dist

    def apsp_dijkstra(self):

        result = np.full((self.vertex.size, self.vertex.size), np.inf)
        count = 0
        for v in self.vertex:
            result[count] = self.sssp_dijkstra(v)
            count = count + 1

        return result
