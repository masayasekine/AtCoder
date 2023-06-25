def main():
    N = int(input())
    S = input()
    T = input()
    for i, s in enumerate(S):
        if s == T[i]:
            continue
        if (s == '1' and T[i] == 'l') or (s == 'l' and T[i] == '1'):
            continue
        if (s == '0' and T[i] == 'o') or (s == 'o' and T[i] == '0'):
            continue
        print('No')
        return
    print('Yes')
main()