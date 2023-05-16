def main():
    N = int(input())
    A = []
    for _ in range(N):
        A.append(int(input()))

    A.sort()
    print(len(set(A)))

main()