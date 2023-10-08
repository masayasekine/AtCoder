N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [list(input()) for _ in range(N)]

# 現状のスコアを計算し、まだ解いていない問題を保存
score_d = {}
unsolved = {}
for i in range(N):
    unsolved[i+1] = []
for i, s in enumerate(S, start=1):
    for j, c in enumerate(s):
        if c == "o":
            S[i-1][j] = A[j]
        if c == "x":
            S[i-1][j] = 0
            unsolved[i].append(A[j])
        if j == 0:
            S[i-1][j] = S[i-1][j] + i
    score_d[i] = sum(S[i-1])

for i in range(N):
    target_score = 0
    # 自分以外の最大値を取得
    for j in range(N):
        if i == j:
            continue
        target_score = max(target_score, score_d[j+1])
    # すでに超えていれば0を追加
    if score_d[i+1] > target_score:
        print(0)
        continue
    # そうでなければ、まだ解いていない問題を何問解けばよいか計算
    # まだ解いていない問題を得点の降順でソート
    unsolved[i+1] = sorted(unsolved[i+1], reverse=True)
    # まだ解いていない問題を順番に解いていき、target_scoreを超えたら終了
    tmp = score_d[i+1]
    count = 0
    for s in unsolved[i+1]:
        count += 1
        tmp += s
        if tmp > target_score:
            print(count)
            break