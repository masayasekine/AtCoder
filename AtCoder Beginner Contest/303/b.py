def main():
    N, M = map(int, input().split())
    A = []
    for _ in range(M):
        A.append(list(map(int, input().split())))
    d = {}
    l = []
    for i in range(N):
        l.append(i+1)
    for i in range(N):
        d[i+1] = l.copy()
    
    for tmp in A:
        for i, a in enumerate(tmp):
            # print(f'tmp: {tmp}, a:{a}, i: {i} d: {d}')
            if a in d[a]:
                d[a].remove(a)
            if i == 0:
                if tmp[i+1] in d[a]:
                    d[a].remove(tmp[i+1])
                continue
            if i >= len(tmp) - 1:
                if tmp[i-1] in d[a]:
                    d[a].remove(tmp[i-1])
                continue
            if tmp[i+1] in d[a]:
                d[a].remove(tmp[i+1])
            if tmp[i-1] in d[a]:
                d[a].remove(tmp[i-1])
    cnt = 0
    for i in range(N):
        cnt += len(d[i+1])
    print(cnt // 2)

main()