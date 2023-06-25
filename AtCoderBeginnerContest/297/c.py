def main():
    H, W = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(str(input()))
    
    cnt = 0
    for s in A:
        bk = ''
        tmp = ''
        for c in s:
            if not bk:
                tmp = tmp + c
                bk = c
                continue
            if c == 'T' and bk == 'T':
                tmp = tmp[:-1] + 'PC'
                bk = 'C'
            else:
                tmp = tmp + c
                bk = c
        print(tmp)

main()


