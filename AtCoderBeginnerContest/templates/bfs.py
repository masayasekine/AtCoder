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