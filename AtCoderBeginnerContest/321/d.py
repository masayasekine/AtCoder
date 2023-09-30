N, M, P = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = []

A.sort()
B.sort()

for i, a in enumerate(A):
    if a > P:
        ans.append(P * ((N - i) * M))
        break
    for j, b in enumerate(B):
        if a + b < P:
            ans.append(a + b)
        else:
            ans.append(P * (M - j))
            break

print(sum(ans))