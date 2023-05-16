def main():
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]

    t = 0
    x = 0
    y = 0

    for l in L:

        t_ = l[0]
        x_ = l[1]
        y_ = l[2]

        n = t_ - t
        # xをx_まで移動する
        n = n - abs(x_ - x)
        if n < 0:
            print('No')
            return
        if n == 0:
            if y == y_:
                t = t_
                x = x_
                y = y_
                continue
            else:
                print('No')
                return

        # 元のyが偶数の時
        if y % 2 == 0:
            # nが偶数の場合、n+y以下の偶数にたどり着ける。奇数ならn+y以下の奇数にたどり着ける
            if n % 2 == 0 and y_ % 2 == 0 and y_ <= n+y:
                t = t_
                x = x_
                y = y_
                continue
            elif n % 2 != 0 and y_ % 2 != 0 and y_ <= n+y:
                t = t_
                x = x_
                y = y_
                continue
        else:
            # nが偶数の場合、n+y以下の奇数にたどり着ける。奇数ならn+y以下の偶数にたどり着ける
            if n % 2 == 0 and y_ % 2 != 0 and y_ <= n+y:
                t = t_
                x = x_
                y = y_
                continue
            elif n % 2 != 0 and y_ % 2 == 0 and y_ <= n+y:
                t = t_
                x = x_
                y = y_
                continue
        print('No')
        return

    print('Yes')

main()