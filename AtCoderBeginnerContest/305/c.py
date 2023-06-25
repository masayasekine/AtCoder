def main():
    H, W = map(int, input().split())
    A = [list(map(str, list(input()))) for _ in range(H)]
    # 2方向以上をクッキーに囲まれた場所を探す？
    for i, line in enumerate(A):
        for j, s in enumerate(line):
            if s == '.':
                cnt = 0
                # 上
                if i != 0 and A[i-1][j] == '#':
                    cnt += 1
                # 右
                if j < len(line) - 1 and A[i][j+1] == '#':
                    cnt += 1
                # 下
                if i < len(A) -1 and A[i+1][j] == '#':
                    cnt += 1
                # 左
                if j != 0 and A[i][j-1] == '#':
                    cnt += 1
                if cnt >= 2:
                    print(f'{i+1} {j+1}')
                    return

main()