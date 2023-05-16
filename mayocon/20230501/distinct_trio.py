N = int(input())
l = list(map(int, input().split()))
 
cnt = 0
for i, m in enumerate(l):
    for j, n in enumerate(l):
        if i >= j or m == n:
            continue
        for k, o in enumerate(l):
            if i >= k or j >= k or m == o or n == o:
                continue
            cnt += 1
print(cnt)