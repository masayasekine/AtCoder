N, X = map(int, input().split())
A = list(map(int, input().split()))

ma = max(A)
A.remove(ma)

if sum(A) >= X:
    print(0)
    exit(0)

mi = min(A)
A.remove(mi)

s = sum(A)


if X - s > 100 or X - s > ma:
    print(-1)
    exit(0)
if X - s <= 0:
    print(0)
    exit(0)
print(X - s)