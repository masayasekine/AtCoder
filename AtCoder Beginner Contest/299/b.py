def main():
    N, T = map(int, input().split())
    C = list(map(int, input().split()))
    R = list(map(int, input().split()))
    if T not in C:
        T = C[0]
    
    max_i = 0
    num = 0
    for i, c in enumerate(C):
        if c == T:
            if R[i] > num:
                max_i = i
                num = R[i]
    print(max_i + 1)
    return

main()