def main():
    N = input()
    l = list(map(int, input().split()))
    result = ''
    for n in l:
        if n % 2 == 0:
            result += str(n)
            result += ' '
    print(result)
main()