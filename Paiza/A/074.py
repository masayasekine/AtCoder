H, W = map(int, input().split())

grid = [list(input()) for _ in range(H)]
print(f'(0, 1):{grid[0][1]}, (0, 0):{grid[0][0]}')
ans = 0

for i, line in enumerate(grid):
    if i <= 0 or i >= H:
        continue
    # print(line)
    if '***' in line:
        for j, p in enumerate(line):
            # 星3つと右上を取れる必要がある
            if j >= W-3:
                continue
            if p == '*' and line[j+1] == '*' and line[j+2] == '*':
                # left_top
                for lt_i in range(i+1, H):
                    for lt_j in range(j):
                        if grid[lt_i][lt_j] == '*':
                            # right_top
                            for rt_i in range(i+1, H):
                                for rt_j in range(j+3, W):
                                    if grid[rt_i][lt_j] == '*':
                                        # bottom_left
                                        for bl_i in range(i):
                                            for bl_j in range(j):
                                                if grid[bl_i][bl_j] == '*':
                                                    # bottom_right
                                                    for br_i in range(i+1, H):
                                                        for br_j in range(j+1, W):
                                                            print(f'({lt_i}, {lt_j}), ({rt_i}, {rt_j}), ({bl_i}, {bl_j}), ({br_i}, {br_j})')
                                                            if grid[br_i][br_j] == '*':
                                                                print(f'({lt_i}, {lt_j}), ({rt_i}, {rt_j}), ({bl_i}, {bl_j}), ({br_i}, {br_j})')
                                                                ans += 1
print(ans)


