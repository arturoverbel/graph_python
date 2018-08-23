import numpy as np


class GraphPro:
    source = []
    target = []
    weight = []
    vertex = []

    undirected = 0

    def __init__(self, source=[], target=[], weight=[], vertex=[]):
        self.source = np.array(source)
        self.target = np.array(target)
        self.weight = np.array(weight)
        self.vertex = np.array(vertex)

        self.set_vertex()

    def print_r(self):
        print("Source: ", self.source)
        print("Target: ", self.target)
        print("Weight: ", self.weight)
        print("Vertex: ", self.vertex)

    @staticmethod
    def probability(x, p):

        x = np.array(x)
        p = np.array(p)
        y = np.random.rand()

        cdf = np.cumsum(p)
        total = len(x)

        pos = 0

        for n in range(total - 1):
            pos = pos + (y >= cdf.item(n))

        return x.item(pos)

    @staticmethod
    def creategraph(total_nodes, pro_edges, weights):

        source = np.array([])
        target = np.array([])
        weight = np.array([])

        for i in range(total_nodes):
            for k in range(total_nodes):
                if k == i:
                    continue

                p = 1 - pro_edges
                has_edge = GraphPro.probability([0, 1], [p, pro_edges])

                if not has_edge:
                    continue

                probabilities = np.zeros(len(weights))
                probabilities = probabilities + (1 / len(weights))
                w = GraphPro.probability(weights, probabilities)

                source = np.append(source, i)
                target = np.append(target, k)
                weight = np.append(weight, w)

        return GraphPro(source, target, weight)

    def set_vertex(self):
        vertex = np.unique(self.source)
        vertex2 = np.unique(self.target)
        self.vertex = np.unique(np.concatenate([vertex, vertex2]))
        return self.vertex

    def set_dynamic_vertex(self, behavior, weights=[1, 2, 3, 4, 5, 6, 7, 8, 9]):

        returned = 0
        found_set = False

        for source in self.vertex:
            for target in self.vertex:
                if source == target:
                    continue

                p = GraphPro.probability([0, 1], [0.5, 0.5])
                if p == 0:
                    continue

                index = np.where(np.logical_and(self.source == source, self.target == target))

                if index[0].size == 0 and (behavior == 'incremental' or behavior == 'full'):
                    probabilities = np.zeros(len(weights))
                    probabilities = probabilities + (1 / len(weights))
                    w = GraphPro.probability(weights, probabilities)

                    returned = self.incremental_vertex(source, target, w)
                    found_set = True

                elif index[0].size > 0 and (behavior == 'decreasing' or behavior == 'full'):
                    returned = self.decreasing_vertex(source, target)
                    found_set = True

                if found_set:
                    break
            if found_set:
                break

        if found_set is False:
            return self.set_dynamic_vertex(behavior, weights)

        return returned

    def decreasing_vertex(self, source, target):

        index = np.where(np.logical_and(self.source == source, self.target == target))[0][0]
        returned = np.array([])

        self.source = np.delete(self.source, index)
        returned = np.append(returned, source)

        self.target = np.delete(self.target, index)
        returned = np.append(returned, target)

        return returned

    def incremental_vertex(self, source, target, weight):

        returned = np.array([])
        self.source = np.append(self.source, source)
        returned = np.append(returned, source)
        self.target = np.append(self.target, target)
        returned = np.append(returned, target)
        self.weight = np.append(self.weight, weight)
        returned = np.append(returned, weight)

        return returned

    def get_weight(self, n1, n2):
        return self.weight[np.logical_and(self.source == n1, self.target == n2)]

    def dijkstra(self, source):

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
