def main():
    S = input()
    T = input()

    target = ['a', 't', 'c', 'o', 'd', 'e', 'r']

    for s in set(S):
        if s in target:
            continue
        if S.count(s) != T.count(s):
            print('No')
            return
    
    conv_cnt_s = S.count('@')
    conv_cnt_t = T.count('@')

    a_s = S.count('a')
    a_t = S.count('a')


main()