def main():
    N = int(input())
    N = str(input())
    tmp = ''
    for s in N:
        if tmp == '':
            tmp = s
            continue
        if s == 'M':
            if tmp == 'M':
                print('No')
                return
        if s == 'F':
            if tmp == 'F':
                print('No')
                return
        tmp = s
    print('Yes')

main()