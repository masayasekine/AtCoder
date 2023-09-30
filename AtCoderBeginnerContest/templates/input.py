# Pythonで入力を受け取るサンプル

## 1桁系
N = int(input())
S = input()

# 複数個の数値をlist型で取得
l = list(map(int, input().split()))

# N行1列の数値
A = []
for _ in range(N):
    A.append(int(input()))
A = [list(map(int, input().split())) for _ in range(M)]
A = [list(map(str, input().split())) for _ in range(M)]


A, B = map(int, input().split())

# tupleをsetに入れる
P = set([tuple(map(int,input().split())) for i in range(M)])

# str, intの入力N行を受け取りtupleにする
A = []
for _ in range(N):
    str_val, int_val = input().split()
    A.append((str_val, int(int_val)))


# 実行時にインプット使用
import io
import sys
_INPUT = """\
7
6 7 2 1 3 4 5
"""
sys.stdin = io.StringIO(_INPUT)