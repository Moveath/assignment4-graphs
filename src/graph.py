from collections import deque
from vertex import Vertex
from edge import Edge
class Graph:
    def __init__(self):
        self.__vertices = {}
        self.__adj_list = {}
    def add_vertex(self, vertex):
        vid = vertex.get_id()
        if vid not in self.__vertices:
            self.__vertices[vid] = vertex
            self.__adj_list[vid] = []
    def add_edge(self, from_id, to_id):
        if from_id not in self.__vertices:
            self.add_vertex(Vertex(from_id))
        if to_id not in self.__vertices:
            self.add_vertex(Vertex(to_id))
        edge = Edge(self.__vertices[from_id], self.__vertices[to_id])
        self.__adj_list[from_id].append(edge)
    def print_graph(self):
        print("Graph (Adjacency List):")
        for vid in sorted(self.__adj_list.keys()):
            neighbors = [e.get_destination().get_id() for e in self.__adj_list[vid]]
            print(f"  {vid} -> {neighbors}")
    def bfs(self, start_id):
        visited = set()
        queue = deque()
        order = []
        visited.add(start_id)
        queue.append(start_id)
        while queue:
            current = queue.popleft()
            order.append(current)
            for edge in self.__adj_list[current]:
                neighbor = edge.get_destination().get_id()
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order
    def dfs(self, start_id):
        visited = set()
        order = []
        def dfs_recursive(vid):
            visited.add(vid)
            order.append(vid)
            for edge in self.__adj_list[vid]:
                neighbor = edge.get_destination().get_id()
                if neighbor not in visited:
                    dfs_recursive(neighbor)
        dfs_recursive(start_id)
        return order