dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def main():
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    
    if grid[0][0] != 's':
        print('No')
        return


    stack = [(0, 0)]
    while stack:
        x, y = stack.pop()

        now = grid[y][x]
        new = ''
        if now == 's':
            new = 'n'
        if now == 's#':
            new = 'n'
        if now == 'n#':
            new = 'u'
        if now == 'u#':
            new = 'k'
        if now == 'k#':
            new = 'e'
        if now == 'e#':
            new = 's'

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < W and 0 <= ny < H and grid[ny][nx] == new:
                if ny == H-1 and nx == W-1:
                    print('Yes')
                    return
                stack.append((nx, ny))
                grid[ny][nx] += '#'

    print('No')

main()