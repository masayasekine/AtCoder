def main():
    A, B = map(int, input().split())
    print('Odd') if A * B % 2 != 0 else print('Even')

main()