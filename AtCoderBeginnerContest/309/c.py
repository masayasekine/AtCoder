N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
A.sort(key=lambda x: (-x[0], x[1]))

cnt = 0
for i, a in enumerate(A):
    cnt += a[1]
    if K < cnt:
        print(a[0]+1)
        exit(0)
print(1)
