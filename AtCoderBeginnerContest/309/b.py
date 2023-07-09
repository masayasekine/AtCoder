N = int(input())
A = []
for _ in range(N):
    A.append([int(char) for char in str(input())])

new_grid = []
for _ in range(N):
    line = []
    for _ in range(N):
        line.append(0)
    new_grid.append(line)

for i in range(N):
    for j in range(N):
        if (i != 0 and i != N -1) and (j != 0 and j != N -1):
            new_grid[i][j] = A[i][j]
            continue
        if i == 0 and j == 0:
            new_grid[i][j] = A[i+1][j]
            continue
        if i == 0:
            new_grid[i][j] = A[i][j-1]
            continue
        if i == N - 1 and j == N - 1:
            new_grid[i][j] = A[i-1][j]
            continue
        if i == N - 1:
            new_grid[i][j] = A[i][j+1]
            continue
        if j == 0:
            new_grid[i][j] = A[i+1][j]
            continue
        if j == N - 1:
            new_grid[i][j] = A[i-1][j]

for line in new_grid:
    print(''.join(map(str, line)))