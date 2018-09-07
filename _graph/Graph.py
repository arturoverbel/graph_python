import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    source = []
    target = []
    weight = []
    vertex = []

    undirected = 0

    def __init__(self, source=[], target=[], weight=[], directed=True):
        self.source = np.array(source)
        self.target = np.array(target)
        self.weight = np.array(weight)
        self.directed = directed

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

    def export(self):
        array_export = [(int(self.source[i]), int(self.target[i]), self.weight[i]) for i in range(self.source.size)]
        return array_export

    def draw(self):
        Gr = nx.DiGraph()
        Gr.add_weighted_edges_from(self.export())
        pos = nx.spring_layout(Gr)
        nx.draw(Gr, pos=pos, with_labels=True, node_size=600)

        edge_labels = dict([((u, v,), d['weight']) for u, v, d in Gr.edges(data=True)])
        nx.draw_networkx_edge_labels(Gr, pos=pos, edge_labels=edge_labels)

        plt.axis('off')
        plt.show()

