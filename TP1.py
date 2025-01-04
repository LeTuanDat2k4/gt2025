# Implement Path-existance and test check for the graph pref prog language where they following behavior:
# 1. As user input 2 nodes
# 2. Return True if path exist and False if not

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)
    
    def path_exists(self, start, end, visited=None):
        visited = [False] * (len(self.graph) + 1)
        visited[start] = True
        newly_visited = [start]
        while newly_visited:
            next_newly_visited = []
            for u in newly_visited:
                for v in self.graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        next_newly_visited.append(v)
            newly_visited = next_newly_visited
        return visited[target]
    
if __name__ == "__main__":
    graph = Graph()
    edges = [(1, 2), (2, 5), (3, 6), (6, 4), (6, 7), (4, 7)]
    for u, v in edges:
        graph.add_edge(u, v)
    input = input("Enter 2 random nodes: ").split()
    start = int(input[0])
    target = int(input[1])
    if graph.path_exists(start, target):
        print("True")
    else:
        print("False")