N = int(input())
A = []
for _ in range(N):
    w, x = input().split()
    A.append((int(w), int(x)))

ans = []
for i in range(24):
    cnt = 0
    low = i
    high = i + 9
    for a in A:
        if a[1] >= low and a[1] < high:
            cnt += a[0]
    ans.append(cnt)
print(max(ans))
