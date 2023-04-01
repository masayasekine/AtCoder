def main():
    N = int(input())
    l = list(map(str, input().split()))
    s = ['and', 'not', 'that', 'the', 'you']
    for n in l:
        if n in s:
            print('Yes')
            return
    print('No')

main()