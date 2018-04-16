class graph_pro:

    source = []
    target = []
    weight = []
    vertex = []

    undirected = 0

    def __init__(self, source = [], target = [], weight = [], vertex = []):
        self.source = source
        self.target = target
        self.weight = weight
        self.vertex = vertex

        self.set_vertex()

    def print(self):
        print("Source: ", self.source)
        print("Target: ", self.target)
        print("Weight: ", self.weight)
        print("Vertex: ", self.vertex)

    def set_vertex(self):
        vertex = set(self.source)
        vertexT = set(self.target) - vertex
        return self.vertex = list(vertex) + list(vertexT)


