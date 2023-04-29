def main():
    N, Y = map(int, input().split())
    for i in range(N+1):
        for j in range(N+1):
            if i + j > N:
                break
            k = N - (i + j)
            if 10000 * i + 5000 * j + 1000 * k == Y:
                print(f'{i} {j} {k}')
                return
    print('-1 -1 -1')

main()