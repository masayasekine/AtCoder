# import io
# import sys
# _INPUT = """\
# 8 5
# 1 3 4 7 8
# """
# sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
A = list(map(int, input().split()))

tmp = 0
for i in range(1,N+1):
    if i > A[tmp]:
        tmp += 1
    print(A[tmp] - i)
