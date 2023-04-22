# Pythonで入力を受け取るサンプル
def main():

    ## 1桁系
    N = int(input())
    S = input()

    ## N行N列の2次元配列
    A = [list(map(int, input().split())) for _ in range(N)]
