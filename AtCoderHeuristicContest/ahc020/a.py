class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        else:
            self.parent[py] = px
            if self.rank[px] == self.rank[py]:
                self.rank[px] += 1

import math

N, M, K = map(int, input().split())
vertices = [list(map(int, input().split())) for _ in range(N)]
edges = [tuple(map(int, input().split())).__add__(tuple([i])) for i in range(M)]
residents = [list(map(int, input().split())) for _ in range(K)]

ans_vertex = ['0']*len(vertices)
ans_edge = ['0']*len(edges)

uf = UnionFind(M)

# 家に対して頂点を回して、全く被らなければ円を大きくする
r = 1
all_bloadcasted = False
use_v = []
while not all_bloadcasted:
    skip = False
    for r_x, r_y in residents:
        found = False
        if skip:
            break

        for i, vertex in enumerate(vertices):
            v_x, v_y = vertex[0], vertex[1]
            # ユークリッド距離
            distance = math.sqrt((v_x - r_x)**2 + (v_y - r_y)**2)
            if distance < r:
                found = True
                ans_vertex[i] = str(r)
                break
        if not found:
            use_v.clear()
            skip = True
            r += 100
            break
    if not skip:
        all_bloadcasted = True

for i in reversed(range(len(edges))):
    if ans_vertex[edges[i][0]-1] == '0' and ans_vertex[edges[i][1]-1] == '0':
        # 未使用の頂点への辺は不要
        del edges[i]

# 重み順ソート・選定
edges.sort(key=lambda x: x[2])
for j, k, m, i in edges:
    if uf.find(j) != uf.find(k):  # 辺を追加しても閉路ができない場合
        uf.union(j, k)
        ans_edge[i] = '1'

# for i, vertex in enumerate(vertices):
#     v_x, v_y = vertex[0], vertex[1]
#     found = False
#     for r_x, r_y in residents:
#         # ユークリッド距離
#         distance = math.sqrt((v_x - r_x)**2 + (v_y - r_y)**2)
#         if distance < 2250:
#             found = True
#     # 範囲内に家なければ出力をOFF
#     if not found:
#         ans_vertex[i] = 0


print(*ans_vertex)
print(*ans_edge)
