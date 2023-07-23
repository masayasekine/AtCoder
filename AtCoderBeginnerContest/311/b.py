
N, D = map(int, input().split())
S = []
for _ in range(N):
    S.append(str(input()))

ans = []
streak = 0
for n in range(D):
    for i, s in enumerate(S):
        if s[n] == 'o':
            if i == N-1:
                streak+=1
            continue
        if s[n] == 'x':
            streak = 0
            break
    ans.append(streak)
print(max(ans))