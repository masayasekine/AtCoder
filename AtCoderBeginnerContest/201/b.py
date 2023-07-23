N = int(input())
A = []
for _ in range(N):
    str_val, int_val = input().split()
    A.append((str_val, int(int_val)))
A.sort(key=lambda x: (-x[1]))
print(A[1][0])