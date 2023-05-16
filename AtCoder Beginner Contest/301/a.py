def main():
    N = int(input())
    S = input()

    t = 0
    a = 0
    for s in S:
        if t >= N:
            print('T')
            return
        elif a >= N:
            print('A')
            return
        if s == 'T':
            t += 1
        elif s == 'A':
            a += 1
    if t > a:
        print('T')
    elif t < a:
        print('A')
    else:
        print('T') if S[-1:] == 'A' else print('A')

main()