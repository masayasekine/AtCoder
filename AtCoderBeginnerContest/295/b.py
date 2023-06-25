def main():
    R, C = map(int, input().split())
    a = [list(map(str, input().split())) for l in range(M)]
    bombs = {}
    for i, m in enumerate(a):
        for j, n in enumerate(m):
            if n not in ['.', '#']:
                bombs[[i, j]] = int(n)
    

