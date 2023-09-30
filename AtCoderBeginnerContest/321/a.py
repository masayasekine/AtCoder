N = str(input())
tmp = 10
for c in N:
    if tmp <= int(c):
        print('No')
        exit(0)
    tmp = int(c)
print('Yes')