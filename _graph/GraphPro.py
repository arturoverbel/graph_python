from _graph.GraphAPSP import GraphAPSP
from _graph.GraphRR import GraphRR
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


class GraphPro(GraphRR):
    def __init__(self, source=[], target=[], weight=[], directed=True):
        GraphRR.__init__(self, source, target, weight, directed)

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

    def kk_incremental(self, dist):
        dist = np.array(dist)

        add = np.full(self.vertex.size-1, np.inf)
        dist = np.vstack([dist, add])
        dist = np.hstack([dist, np.append(add, np.inf)[:,None]])

        z = self.node_incremental['node']
        T1 = self.node_incremental['source']
        T2 = self.node_incremental['target']

        for k_in in T1:
            dist[self.vertex == z, self.vertex == k_in] = self.get_weight(k_in, z)

        for k_out in T2:
            dist[self.vertex == k_out, self.vertex == z] = self.get_weight(z, k_out)

        min_in_z = {}
        min_out_z = {}

        for v in self.vertex:
            for k_in in T1:
                if v == k_in:
                    continue
                L_vz = dist[self.vertex == v, self.vertex == k_in][0] + self.get_weight(k_in, z)
                if v not in min_in_z or L_vz < min_in_z[v]:
                    min_in_z[v] = L_vz
            for k_out in T2:
                if v == k_out:
                    continue

                L_zv = dist[self.vertex == k_out, self.vertex == v][0] + self.get_weight(z, k_out)
                if v not in min_out_z or L_zv < min_out_z[v]:
                    min_out_z[v] = L_zv

        print(min_in_z)
        print(min_out_z)
        for i, L_iz in min_in_z.items():
            for j, L_jz in min_out_z.items():
                print('------------------')
                print(i, ": ", L_iz)
                print(j, ": ", L_jz)
                print("actual: ", )
                print(dist[self.vertex == i, self.vertex == j][0])
                if L_iz + L_jz < dist[self.vertex == i, self.vertex == j][0]:
                    print('Entro !!')
                    dist[self.vertex == i, self.vertex == j] = L_iz + L_jz
                print('------------------')

        return dist
        for i, value in min_in_z.items():
            dist[self.vertex == z, self.vertex == i] = value
        for j, value in min_out_z.items():
            dist[self.vertex == j, self.vertex == z] = value

    def draw(self, with_weight=True):
        gr = nx.DiGraph()
        gr.add_weighted_edges_from(self.export())
        pos = nx.spring_layout(gr)
        list_edges = list(gr.edges())
        last = ()

        if self.last_vertex_modified.size > 0:
            last = (int(self.last_vertex_modified[0]), int(self.last_vertex_modified[1]))
            list_edges.remove(last)
            if not self.directed:
                list_edges.remove((int(self.last_vertex_modified[1]), int(self.last_vertex_modified[0])))

        nx.draw(gr, pos=pos, with_labels=True, edgelist=list_edges, node_size=600)

        if with_weight:
            edge_labels = dict([((u, v,), d['weight']) for u, v, d in gr.edges(data=True)])
            nx.draw_networkx_edge_labels(gr, pos=pos, edgelist=list_edges, edge_labels=edge_labels)

        if len(last) > 0:
            nx.draw_networkx_edges(gr, pos=pos, edgelist=[last], width=2.0, edge_color='b')

        plt.axis('off')
        plt.show()
