from collections import deque

def bfs(graph, root):
    visited = set()
    queue = deque([(root, 0)])
    max_distance = 0
    farthest_node = root

    while queue:
        node, distance = queue.popleft()
        if node not in visited:
            visited.add(node)
            if distance > max_distance:
                max_distance = distance
                farthest_node = node
            for neighbor in graph[node]:
                queue.append((neighbor, distance + 1))

    return farthest_node, max_distance

N1, N2, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

graph = {}
for i in range(N1 + N2):
    graph[i+1] = []
for a in A:
    graph[a[0]].append(a[1])
    graph[a[1]].append(a[0])

farthest_node_a, max_distance_a = bfs(graph, 1)
farthest_node_b, max_distance_b = bfs(graph, N1 + N2)

print(max_distance_a + max_distance_b + 1)
