def main():
    N = int(input())
    if N % 5 == 0:
        print(N)
        return
    if N % 5 < 3:
        print(N - (N % 5))
        return
    else:
        print(N + (5 - (N % 5)))
        return

main()