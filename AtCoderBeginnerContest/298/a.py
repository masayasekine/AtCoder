def main():
    _ = int(input()) 
    S = input()
    good = False
    bad = False
    for s in S:
        if s == 'o':
            good = True
        elif s == 'x':
            bad = True
    if good and not bad:
        print('Yes')
        return
    print('No')
    return
main()
