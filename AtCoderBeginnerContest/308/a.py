def main():
    l = list(map(int, input().split()))
    tmp = 0
    for i in l:
        if tmp > i:
            print('No')
            return
        if i < 100 or i > 675:
            print('No')
            return
        if i % 25 != 0:
            print('No')
            return
        tmp = i
    print('Yes')


main()