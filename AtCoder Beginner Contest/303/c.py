def main():
    # setを使いましょう
    N, M, H, K = map(int, input().split())
    S = input()
    X = []
    Y = []
    # for _ in range(M):
    #     A, B = map(int, input().split())
    #     X.append(A)
    #     Y.append(B)
    A = []
    for _ in range(M):
        A.append(list(map(int, input().split())))
    B = set(A)
    

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
            if x not in X or y not in Y:
                continue
            tmp = [x,y]
            if tmp in B:
                H = K
                A.remove(tmp)
            # for i, a in enumerate(X):
            #     if x == a:
            #         if y == Y[i]:
            #             H = K
            #             del X[i]
            #             del Y[i]
            #             break

    print('Yes')
main()