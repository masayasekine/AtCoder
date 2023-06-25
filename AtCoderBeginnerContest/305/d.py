_ = int(input())
l = list(map(int, input().split()))
Q = int(input())
A = [list(map(int, input().split())) for _ in range(Q)]

slp = ''
for i, time in enumerate(l):
    if i == 0:
        continue
    if i % 2 == 0:
        slp += '0' * (time - l[i-1])
    if i % 2 != 0:
        slp += '1' * (time - l[i-1])

for a in A:
    start = a[0]
    end = a[1]
    print(slp[start:end].count('0'))