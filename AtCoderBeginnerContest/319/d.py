import io
import sys
_INPUT = """\
10 1
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
L = list(map(int, input().split()))

def is_enough_lines(width):
    current_line = 1
    current_line_length = 0
    for word in L:
        if current_line_length + word > width:
            current_line += 1
            if current_line > M:
                return False
            current_line_length = word
        else:
            current_line_length += word
            if current_line_length < width:
                current_line_length += 1 # 単語の区切りスペースを追加
    return True

def find_smallest_satisfying_value():
    # 二分探索の初期設定
    lower_bound = 0  # 下限
    upper_bound = 10000000009  # 上限（適切な大きな値を設定）

    while lower_bound < upper_bound:
        mid = (lower_bound + upper_bound) // 2  # 中間値を計算

        if is_enough_lines(mid):
            upper_bound = mid  # 条件を満たす場合、上限を中間値に設定
        else:
            lower_bound = mid + 1  # 条件を満たさない場合、下限を中間値の次の値に設定

    return lower_bound
    
print(find_smallest_satisfying_value())
