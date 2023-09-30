class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, u, v, w):
        if u not in self.edges:
            self.edges[u] = []
        if v not in self.edges:
            self.edges[v] = []
        self.edges[u].append((v, w))
        self.edges[v].append((u, w))

    def find_max_path(self, start):
        def dfs(node, visited, current_weight):
            max_weight = current_weight

            for neighbor, weight in self.edges.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    max_weight = max(max_weight, dfs(neighbor, visited, current_weight + weight))
                    visited.remove(neighbor)

            return max_weight

        return dfs(start, {start}, 0)

N, M = map(int, input().split())

graph = Graph()
for _ in range(M):
    u, v, w = map(int, input().split())
    graph.add_edge(u, v, w)

total_weights = [graph.find_max_path(i+1) for i in range(N)]

print(max(total_weights))
