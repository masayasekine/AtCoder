N = int(input())
S = [input() for _ in range(N)]
count_d = {}

# s内のoの文字数をカウントして、count_dに格納
for i, s in enumerate(S, start=1):
    count_d[i] = s.count("o")

# count_dをvalueの降順でソート(同値の場合はkeyの昇順)
count_d = sorted(count_d.items(), key=lambda x: x[1], reverse=True)

# keyのリストを取得
key_list = []
for c in count_d:
    key_list.append(c[0])

# key_listをスペース区切りで出力
print(*key_list)