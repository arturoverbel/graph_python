import numpy as np
from _graph.GraphAPSP import GraphAPSP


class GraphRR(GraphAPSP):

    def __init__(self, source=[], target=[], weight=[], directed=True):
        GraphAPSP.__init__(self, source, target, weight, directed)

    def dijkstra_truncated(self, dist_s):
        u = self.last_vertex_modified[0]
        v = self.last_vertex_modified[1]
        w_uv = self.last_vertex_modified[2]

        dist_s = np.array(dist_s)
        if dist_s[self.vertex == v] <= dist_s[self.vertex == u] + w_uv:
            return

        dist_s[self.vertex == v] = dist_s[self.vertex == u] + w_uv
        PQ = {v: dist_s[v]}

        while len(PQ) > 0:
            (y, weight) = min(PQ.items(), key=lambda x: x[1])
            PQ.pop(y)
            for w in self.target[self.source == y]:
                if dist_s[self.vertex == w] <= weight + self.get_weight(y, w):
                    continue

                new_weight = weight + self.get_weight(y, w)
                dist_s[self.vertex == w] = new_weight
                PQ[w] = new_weight

        return dist_s

    def bfs_truncated(self, source, dist):
        u = self.last_vertex_modified[0]
        v = self.last_vertex_modified[1]
        w_uv = self.last_vertex_modified[2]

        dist = np.array(dist)
        if dist[self.vertex == source, self.vertex == v] <= dist[self.vertex == source, self.vertex == u] + w_uv:
            return dist

        dist[self.vertex == source, self.vertex == v] = dist[self.vertex == source, self.vertex == v] + w_uv

        PQ = np.array([v])
        vis = {v: True}

        while len(PQ) > 0:
            y, PQ = PQ[-1], PQ[:-1]
            dist[self.vertex == source, self.vertex == y] = \
                dist[self.vertex == source, self.vertex == u] + w_uv + dist[self.vertex == v, self.vertex == y]
            for w in self.target[self.source == y]:
                if (w not in vis or not vis[w]) \
                        and dist[self.vertex == source, self.vertex == w] > \
                        dist[self.vertex == source, self.vertex == u] + w_uv + dist[self.vertex == v, self.vertex == w]:
                    vis[w] = True
                    PQ = np.append(PQ, [w])

        return dist

    def bfs_truncated_each_node(self, dist):
        dist = np.array(dist)
        for vertex in self.vertex:
            dist = self.bfs_truncated(vertex, dist.tolist())

        return dist

    def bfs_truncated_with_sources(self, dist):
        dist = np.array(dist)
        for source in self.find_source_affected(dist.tolist()):
            dist = self.bfs_truncated(source, dist)

        return dist

    def find_source_affected(self, dist):
        dist = np.array(dist)
        u = self.last_vertex_modified[0]
        v = self.last_vertex_modified[1]
        w_uv = self.last_vertex_modified[2]

        source_affected = np.array([])
        dist = np.array(dist)
        if dist[self.vertex == u, self.vertex == v] <= w_uv + [0]:
            return source_affected

        dist[self.vertex == u, self.vertex == v] = dist[self.vertex == u, self.vertex == v] + w_uv

        PQ = np.array([v])
        vis = {v: True}

        while len(PQ) > 0:
            x, PQ = PQ[-1], PQ[:-1]
            for z in self.source[self.target == x]:
                if (z not in vis or not vis[z]) \
                        and dist[self.vertex == z, self.vertex == v] > \
                        dist[self.vertex == z, self.vertex == u] + w_uv:
                    vis[z] = True
                    PQ = np.append(PQ, [z])
                    source_affected = np.append(source_affected, [z])

        return source_affected


