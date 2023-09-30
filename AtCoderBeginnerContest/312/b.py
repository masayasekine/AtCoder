def is_tak_code(x, y):
    # 左上
    for n in range(4):
        for m in range(4):
            # print(f'x+{n}: {x+n}, y+{m}: {y+m}')
            if n == 3 or m == 3:
                if S[x+n][y+m] != '.':
                    return False
            else:
                if S[x+n][y+m] != '#':
                    return False
    # 右下
    for n in range(3):
        for m in range(3):
            if n == 0 or m == 0:
                if S[x+n+5][y+m+5] != '.':
                    return False
            else:
                if S[x+n+6][y+m+6] != '#':
                    return False
    return True

N, M = map(int, input().split())
S = [input() for _ in range(N)]
ans = []
for x, s in enumerate(S):
    for y, c in enumerate(s):
        if x+8 > N or y+8 > M:
            continue
        if c != '#':
            continue
        if is_tak_code(x, y):
            ans.append([x+1, y+1])

for a in ans:
    print(*a)
