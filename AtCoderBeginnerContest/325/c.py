from collections import deque

def bfs(i, j, grid, visited, H, W):
    queue = deque([(i, j)])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] == '#' and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

def count_clusters(grid, H, W):
    visited = [[False for _ in range(W)] for _ in range(H)]
    count = 0
    
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#' and not visited[i][j]:
                bfs(i, j, grid, visited, H, W)
                count += 1
                
    return count

H, W = map(int, input().split())
grid = [input() for _ in range(H)]

ans = count_clusters(grid, H, W)

print(ans)