class Graph:
    def __init__(self):
        # Initialize the graph as an adjacency list (dictionary of lists)
        self.adjacency_list = {}

    def add_edge(self, u, v):
        """Adds an edge between vertex u and vertex v."""
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)  

    def dfs(self, start_vertex):
        """Performs a Depth-First Search (DFS) starting from start_vertex."""
        visited = set() 
        traversal_order = []  

        def dfs_recursive(vertex):
            """Recursive helper function for DFS."""
            visited.add(vertex)  
            traversal_order.append(vertex)  
            for neighbor in self.adjacency_list.get(vertex, []):
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        
        dfs_recursive(start_vertex)

        print("DFS Traversal Order:", traversal_order)

if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 5)
    g.add_edge(5, 6)

    print("Graph Adjacency List:", g.adjacency_list)
    g.dfs(1)  
