import networkx as nx

class graph:

    graph = nx.DiGraph()
    distances = {}

    def floyd_warshall(self):
        nodes = list(self.graph.nodes)

        for i in nodes:
            dict_i = {}
            for j in nodes:
                if i == j:
                    dict_i[j] = 0
                    continue

                try:
                    dict_i[j] = self.graph[i][j]['weight']
                except:
                    dict_i[j] = float("inf")

            self.distances[i] = dict_i

        for i in nodes:
            for j in nodes:
                for k in nodes:
                    ij = self.distances[i][j]
                    ik = self.distances[i][k]
                    kj = self.distances[k][j]

                    if ij > ik + kj:
                        self.distances[i][j] = ik + kj

        return self.distances


    def dijkstra(self):
        nodes = list(self.graph.nodes)

        for i in nodes: #Set first values
            dict_i = {}
            for j in nodes:
                if i == j:
                    dict_i[j] = 0
                else:
                    dict_i[j] = float("inf")
            self.distances[i] = dict_i

        for oneNode in nodes: #Start algoritm
            Q = []
            for node in nodes: Q.append(node)

            while len(Q) != 0:
                v = 0
                min = float("inf")
                for node_q in Q:
                    if self.distances[oneNode][node_q] <= min:
                        min = self.distances[oneNode][node_q]
                        v = node_q

                Q.remove(v)

                neighbors = list(self.graph.neighbors(v))

                for neighborV in neighbors:
                    w = self.graph[v][neighborV]['weight']
                    alt = self.distances[oneNode][v] + w
                    if alt < self.distances[oneNode][neighborV]:
                        self.distances[oneNode][neighborV] = alt

        return self.distances



    def print_distances(self):
        printt = ""
        for i in self.distances:
            printt = printt + str(i) + ": \t"
            for j in self.distances[i]:
                printt = printt + str(self.distances[i][j]) + "\t"
            printt = printt + "\n"
        print("\n------------------------------------")
        print(printt)
        return



    def create_network(self, source, target, weight):

        self.graph = nx.DiGraph()
        count = len(source)

        edges = []

        for i in range(0, count):
            edges.append( (source[i], target[i], weight[i]) )

        self.graph.add_weighted_edges_from(edges)
        return self.graph

    def setGraph(self, g):
        self.graph = g

    def edges( self ):

        retorno = []

        for n, nbrs in self.graph.adjacency():
            for nbr, eattr in nbrs.items():
                data = eattr['weight']
                retorno.append([ n, nbr, data])

        return retorno