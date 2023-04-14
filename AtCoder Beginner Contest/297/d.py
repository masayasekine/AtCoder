def main():
    A, B = map(int, input().split())
    cnt = -1
    while B:
        if A < B:
            A, B = B, A
        cnt = A // B
        A %= B
    print(cnt)

main()