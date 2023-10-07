N, M, P = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = []

A.sort()
B.sort()

# 前からi個の和を事前に求めておく
l = [0] * (M + 1)
for i, b in enumerate(B, start=1):
    l[i] = sum(B[:i])
print(l)

# TODO: ソートしたBのどこでPを超えるかを求める


print(sum(ans))