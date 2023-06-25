def main():
    N, D = map(int, input().split())
    l = list(map(int, input().split()))
    bk = 0
    for n in l:
        if bk != 0 and n - bk <= D:
            print(n)
            return
        bk = n
    print(-1)

main()