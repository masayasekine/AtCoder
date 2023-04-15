def main():
    A, B = map(int, input().split())
    cnt = -1
    if A < B:
        A, B = B, A
    while B:
        cnt += A // B
        A %= B
        A, B = B, A
    print(cnt)

main()