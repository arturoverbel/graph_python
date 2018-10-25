import numpy as np
from _graph.GraphRR import GraphRR


class GraphKNNB(GraphRR):

    def __init__(self, source=[], target=[], weight=[], directed=True):
        GraphRR.__init__(self, source, target, weight, directed)

    def knnb_node_incremental(self, dist):
        dist = np.array(dist)

        add = np.full(self.vertex.size-1, np.inf)
        dist = np.vstack([dist, add])
        dist = np.hstack([dist, np.append(add, np.inf)[:, None]])
        dist[self.vertex.size-1, self.vertex.size-1] = 0

        z = self.node_incremental['node']
        T1 = self.node_incremental['source']
        T2 = self.node_incremental['target']

        min_in_z = {}
        min_out_z = {}

        for k_in in T1:
            dist[self.vertex == k_in, self.vertex == z] = self.get_weight(k_in, z)

        for k_out in T2:
            dist[self.vertex == z, self.vertex == k_out] = self.get_weight(z, k_out)

        for v in self.vertex:
            if v == z:
                continue
            for k_in in T1:
                #if v == k_in:
                #    continue
                L_vz = dist[self.vertex == v, self.vertex == k_in][0] + self.get_weight(k_in, z)
                if v not in min_in_z or L_vz < min_in_z[v]:
                    min_in_z[v] = L_vz
            for k_out in T2:
                #if v == k_out:
                #    continue

                L_zv = dist[self.vertex == k_out, self.vertex == v][0] + self.get_weight(z, k_out)
                if v not in min_out_z or L_zv < min_out_z[v]:
                    min_out_z[v] = L_zv
        for i, L_iz in min_in_z.items():
            for j, L_jz in min_out_z.items():
                if i == j:
                    continue
                if L_iz + L_jz < dist[self.vertex == i, self.vertex == j][0]:
                    dist[self.vertex == i, self.vertex == j] = L_iz + L_jz

        for i, value in min_in_z.items():
            dist[self.vertex == i, self.vertex == z] = value
        for j, value in min_out_z.items():
            dist[self.vertex == z, self.vertex == j] = value

        return dist


