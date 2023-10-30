import math
import itertools

def is_square(n):
    return math.sqrt(n) % 1 == 0

N = int(input())
S = input()
# 各桁の出現する回数をカウント
counter = [0] * 10
for s in S:
    counter[int(s)] += 1

def get_squares_up_to_n(n):
    i = 1
    squares = []
    while i * i <= n:
        squares.append(i * i)
        i += 1
    return squares

# 上限を設定
n = int(''.join(['9'] * N))
squares = get_squares_up_to_n(n)

ans = 0
for square in squares:
    # 各桁の出現する回数をカウント
    tmp_counter = [0] * 10
    for s in str(square):
        tmp_counter[int(s)] += 1
    # 同じ桁の数が同じ数だけ含まれているか判定。
    if tmp_counter == counter:
        ans += 1
    else:
        # 0は任意の数に変更可能
        tmp_zero = counter[0]
        for i in range(tmp_zero):
            counter[0] -= 1
            if tmp_counter == counter:
                print(square)
                ans += 1
        counter[0] = tmp_zero

print(ans)