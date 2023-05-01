def main():
    H, W = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(input())

    size = []
    for i, a in enumerate(A):
        for j, s in enumerate(a):
            if s == '#':
                # 左下が.ならカウントしない
                if i == H-1 or j == 0 or A[i+1][j-1] == '.':
                    continue
                # 右上が#ならカウントしない
                if i != 0 and j != W-1 and A[i-1][j+1] == '#':
                    continue
                tmp = 1
                tmp_i = i
                tmp_j = j
                while tmp_i < H-1 and tmp_j >= 0:
                    # グリッドの左下を判定する
                    tmp_i += 1
                    tmp_j -= 1
                    if A[tmp_i][tmp_j] == '#':
                        tmp += 1
                    else:
                        break
                # 繋がる#の数-1/2がバツ印のサイズになる
                size.append((tmp-1) // 2)
    ans = []
    for i in range(1, min(H,W)+1):
        ans.append(size.count(i))
    print(*ans)

main()