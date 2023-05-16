def main():
    _, A, B = map(int, input().split())
    l = list(map(int, input().split()))

    ans = A + B
    for i, c in enumerate(l):
        if ans == c:
            print(i + 1)

main()