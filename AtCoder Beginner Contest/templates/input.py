# Pythonで入力を受け取るサンプル
def main():

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

    ## N行N列の2次元配列
    A = [list(map(int, input().split())) for _ in range(N)]

    A, B = map(int, input().split())

    # tupleをsetに入れる
    P = set([tuple(map(int,input().split())) for i in range(M)])