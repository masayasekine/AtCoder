def main():
    _ = int(input())
    A = list(map(int, input().split()))
    flag = False
    while not flag:
        for i, a in enumerate(A):
            if i == len(A)-1:
                break
            next = A[i+1]
            n = a - next
            if n == -1 or n == 1:
                flag = True
                continue
            else:
                flag = False
                l = []
                if n < 0:
                    for j in range(1, abs(n)):
                        l.append(a + j)
                if n > 0:
                    for j in range(1, abs(n)):
                        l.append(a - j)
                A[i+1:i+1] = l
                break
    print(*A)
main()