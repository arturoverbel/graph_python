import numpy as np
from _graph.Graph import Graph


class DynamicGraph(Graph):
    def __init__(self, source=[], target=[], weight=[], directed=True):
        Graph.__init__(self, source, target, weight, directed)
        self.last_vertex_modified = np.array([])

    def dynamic_decreasing_random_vertex(self):

        count_max = 100
        flag = 0
        while True:
            source = np.random.choice(self.vertex, 1)[0]
            choisen = self.target[source == self.source]
            if choisen.size != 0:
                target = np.random.choice(choisen, 1)[0]
                break
            flag = flag + 1
            if flag >= count_max:
                return -2

        return self.dynamic_decreasing_vertex(source, target)

    def dynamic_decreasing_vertex(self, source, target):

        index = np.where(np.logical_and(self.source == source, self.target == target))[0][0]
        returned = np.array([])

        self.source = np.delete(self.source, index)
        returned = np.append(returned, source)

        self.target = np.delete(self.target, index)
        returned = np.append(returned, target)

        self.weight = np.delete(self.weight, index)

        self.last_vertex_modified = returned

        return returned

    def dynamic_incremental_random_vertex(self, weights=[1, 2, 3, 4, 5, 6, 7, 8, 9]):

        count_max = 100
        flag = 0
        while True:
            source = np.random.choice(self.vertex, 1)[0]
            index_for_target = np.invert(np.logical_or(np.in1d(self.vertex, self.target[source == self.source]), self.vertex == source))

            choisen = self.vertex[index_for_target]
            if choisen.size != 0:
                target = np.random.choice(choisen, 1)[0]
                break
            flag = flag + 1
            if flag >= count_max:
                return -2

        w = np.random.choice(weights)
        return self.dynamic_incremental_vertex(source, target, w)

    def dynamic_incremental_vertex(self, source, target, weight=1):

        returned = np.array([])
        self.source = np.append(self.source, source)
        returned = np.append(returned, source)
        self.target = np.append(self.target, target)
        returned = np.append(returned, target)
        self.weight = np.append(self.weight, weight)
        returned = np.append(returned, weight)

        self.last_vertex_modified = returned

        return returned

    def vertex_update(self, source, target, weight=1):
        self.weight[np.logical_and(self.source == source, self.target == target)] = weight
        if not self.directed:
            self.weight[np.logical_and(self.source == target, self.target == source)] = weight

        self.last_vertex_modified = np.array([source, target, weight])
        return True

    def vertex_update_random(self, weight=1):
        count_max = 100
        flag = 0
        while True:
            source = np.random.choice(self.vertex, 1)[0]
            index_for_target = np.logical_or(np.in1d(self.vertex, self.target[source == self.source]), self.vertex == source)
            choisen = self.vertex[index_for_target]

            if choisen.size != 0:
                target = np.random.choice(choisen, 1)[0]
                if self.get_weight(source, target) > 1:
                    break

            flag = flag + 1
            if flag >= count_max:
                return -2

        return self.vertex_update(source, target, weight=weight)
