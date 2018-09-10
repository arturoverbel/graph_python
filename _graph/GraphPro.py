from _graph.GraphAPSP import GraphAPSP
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


class GraphPro(GraphAPSP):

    def __init__(self, source=[], target=[], weight=[], directed=True):
        GraphAPSP.__init__(self, source, target, weight, directed)

    @staticmethod
    def creategraph(total_nodes, pro_edges, weights, directed=True):

        source = np.array([])
        target = np.array([])
        weight = np.array([])

        for i in range(total_nodes):
            for k in range(i+1, total_nodes):
                if k == i:
                    continue

                p = 1 - pro_edges
                has_edge = np.random.choice(2, 1, p=[p, pro_edges])[0]

                if not has_edge:
                    continue

                probabilities = np.zeros(len(weights))
                probabilities = probabilities + (1 / len(weights))
                w = np.random.choice(weights, 1, p=probabilities)[0]

                source = np.append(source, i)
                target = np.append(target, k)
                weight = np.append(weight, w)

                if not directed:
                    source = np.append(source, k)
                    target = np.append(target, i)
                    weight = np.append(weight, w)

        return GraphPro(source, target, weight)

    def draw(self, with_weight=True):
        Gr = nx.DiGraph()
        Gr.add_weighted_edges_from(self.export())
        pos = nx.spring_layout(Gr)
        list_edges = list(Gr.edges())
        last = ()

        if self.last_vertex_modified.size > 0:
            last = (int(self.last_vertex_modified[0]), int(self.last_vertex_modified[1]) )
            list_edges.remove(last)

        nx.draw(Gr, pos=pos, with_labels=True, edgelist=list_edges, node_size=600)

        if with_weight:
            edge_labels = dict([((u, v,), d['weight']) for u, v, d in Gr.edges(data=True)])
            nx.draw_networkx_edge_labels(Gr, pos=pos, edgelist=list_edges, edge_labels=edge_labels)

        if len(last) > 0:
            nx.draw_networkx_edges(Gr, pos=pos, edgelist=[last], width=2.0, edge_color='b')

        plt.axis('off')
        plt.show()
