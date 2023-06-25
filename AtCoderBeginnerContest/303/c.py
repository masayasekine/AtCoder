def main():
    N, M, H, K = map(int, input().split())
    S = input()
    P = set([tuple(map(int,input().split())) for i in range(M)])
    

    x = 0
    y = 0
    for s in S:
        H -= 1
        if s == 'R':
            x += 1
        if s == 'L':
            x -= 1
        if s == 'U':
            y += 1
        if s == 'D':
            y -= 1
        if H < 0:
            print('No')
            return
        if H < K:
            if (x,y) in P:
                H = K
                P.remove((x,y))

    print('Yes')
main()