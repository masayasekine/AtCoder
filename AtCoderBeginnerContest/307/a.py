_ = int(input())
A = list(map(int, input().split()))

step = 0
ans = []
for i, day in enumerate(A, start=1):
    step += day
    if i % 7 == 0:
        ans.append(step)
        step = 0
print(*ans)

