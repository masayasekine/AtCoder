def main():
    N = int(input())
    l = list(map(int, input().split()))
    
    cnt = 0
    while True:
        for i, n in enumerate(l):
            if n % 2 != 0:
                print(cnt)
                return
            l[i] = n // 2
        cnt += 1


main()