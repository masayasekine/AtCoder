_ = int(input())
l = list(map(int, input().split()))

for i, n in enumerate(l):
    if i > 0 and n != l[i-1]:
        print('No')
        exit()
print('Yes')