import numpy as np


class Graph:
    source = []
    target = []
    weight = []
    vertex = []

    undirected = 0

    def __init__(self, source=[], target=[], weight=[]):
        self.source = np.array(source)
        self.target = np.array(target)
        self.weight = np.array(weight)

        self.set_vertex()

    def print_r(self):
        print("Source: ", self.source)
        print("Target: ", self.target)
        print("Weight: ", self.weight)
        print("Vertex: ", self.vertex)

    def set_vertex(self):
        vertex = np.unique(self.source)
        vertex2 = np.unique(self.target)
        self.vertex = np.unique(np.concatenate([vertex, vertex2]))
        return self.vertex

    def get_weight(self, n1, n2):
        return self.weight[np.logical_and(self.source == n1, self.target == n2)]
