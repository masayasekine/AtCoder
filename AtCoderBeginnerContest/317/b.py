N = int(input())
A = list(map(int, input().split()))
A.sort()
for i, a in enumerate(A):
    if a + 1 < A[i+1]:
        print(a+1)
        exit(0)