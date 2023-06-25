def main():
    N = int(input())
    if N < 2:
        print(0)
        return
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    matched = False

    for i in range(1, len(a)):
        if matched:
            matched = False
            continue
        print(f'm: {a[i]}, n: {a[i-1]}')
        if a[i] == a[i-1]:
            matched = True
            cnt += 1
    print(cnt)

main()


