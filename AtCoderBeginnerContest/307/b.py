
def main():
    M = int(input())
    A = []
    for _ in range(M):
        A.append(str(input()))
    for i in range(M):
        for j in range(M):
            if i == j:
                continue
            concut = A[i] + A[j]
            if concut == concut[::-1]:
                print('Yes')
                return
    print('No')

main()