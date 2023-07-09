def main():
    N, M = map(int, input().split())
    C = list(map(str, input().split()))
    D = list(map(str, input().split()))
    P = list(map(int, input().split()))
    price = {}
    price['nothing'] = P[0]
    for i, color in enumerate(D):
        price[color] = P[i+1]
    
    ans = 0
    for color in C:
        if color in price.keys():
            ans += price[color]
        else:
            ans += price['nothing']
    print(ans)


main()