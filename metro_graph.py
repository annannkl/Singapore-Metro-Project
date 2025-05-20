# === Metro Graph Data Structures ===

class Vertex:
    def __init__(self, key):
        self.key = key
        self.data = None
        self.edges = []
        self.parent = None
        self.color = 'white'
        self.distance = float("inf")

    def display(self):
        print("\n📍 Vertex Info")
        print("═" * 40)
        print(f"🔑 Code      : {self.key}")
        print(f"🏷️  Name      : {self.data}")
        print(f"📏 Distance  : {self.distance}")
        print("🔗 Connections:", end=" ")
        if self.edges:
            print(", ".join([e.connection.key for e in self.edges]))
        else:
            print("None")
        print("═" * 40)


class Edge:
    def __init__(self, vertex):
        self.connection = vertex
        self.weight = 1


class Graph:
    def __init__(self):
        self.vertices = {}
        self.directed = False
        self.queue = []
        self.start = None

    def init_bfs(self):
        for v in self.vertices.values():
            v.parent = None
            v.distance = float("inf")
            v.color = 'white'

    def relax(self, va, vb, w):
        if va.distance + w < vb.distance:
            vb.distance = va.distance + w
            vb.parent = va

    def dijkstra(self, start):
        self.start = start
        self.init_bfs()
        if start not in self.vertices:
            print(f"\n❌ Start station '{start}' not found.")
            return False
        v = self.vertices[start]
        v.distance = 0
        Q = list(self.vertices.values())
        while Q:
            Q.sort(key=lambda v: v.distance)
            mv = Q.pop(0)
            for e in mv.edges:
                self.relax(mv, e.connection, e.weight)
        return True

    def bfs(self, start):
        self.start = start
        self.init_bfs()
        if start not in self.vertices:
            print(f"\n❌ Start station '{start}' not found.")
            return False
        v = self.vertices[start]
        v.distance = 0
        v.color = 'gray'
        self.queue = [v]
        while self.queue:
            v = self.queue.pop(0)
            v.color = 'black'
            for e in v.edges:
                con = e.connection
                if con.color == 'white':
                    con.color = 'gray'
                    con.distance = v.distance + 1
                    con.parent = v
                    self.queue.append(con)
        return True

    def bfs_shortest_path(self, dest):
        if dest not in self.vertices:
            print(f"\n❌ Destination station '{dest}' not found.")
            return False
        v = self.vertices[dest]
        if v.parent is None and dest != self.start:
            print(f"\n⚠️ No path from {self.vertices[self.start].data} to {v.data}")
            return False
        path = []
        self._build_path(v, path)
        print("\n🧭 Route Found:")
        print("➡️  " + " ➡️  ".join([node.data for node in path]))
        print(f"\n🛑 Total Stops: {len(path)-1}")
        return True

    def print_dijkstra_path(self, dest):
        if dest not in self.vertices:
            print(f"\n❌ Destination station '{dest}' not found.")
            return False
        v = self.vertices[dest]
        if v.parent is None and dest != self.start:
            print(f"\n⚠️ No path from {self.vertices[self.start].data} to {v.data}")
            return False
        path = []
        self._build_path(v, path)
        print("\n🧭 Route Found:")
        print("➡️  " + " ➡️  ".join([node.data for node in path]))
        print(f"\n⏱️  Total Time: {v.distance} minutes")
        return True

    def _build_path(self, vertex, path_list):
        if vertex.parent is not None:
            self._build_path(vertex.parent, path_list)
        path_list.append(vertex)

    def add(self, key):
        if key in self.vertices:
            return self.vertices[key]
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex
        return new_vertex

    def connect(self, key_a, key_b, **kwargs):
        if key_a not in self.vertices or key_b not in self.vertices:
            return False, "Key not found"
        weight = kwargs.get('weight', 1)
        va = self.vertices[key_a]
        vb = self.vertices[key_b]
        edge = Edge(vb)
        edge.weight = weight
        va.edges.append(edge)
        if not self.directed:
            edge = Edge(va)
            edge.weight = weight
            vb.edges.append(edge)
        return True, "Connected"
