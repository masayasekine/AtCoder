N, M = map(int, input().split())
S = input()
T = input()
ans = 3
if T[:N] == S:
    if T[M-N:] == S:
        ans = 0
    else:
        ans = 1
elif T[M-N:] == S:
    ans = 2
print(ans)