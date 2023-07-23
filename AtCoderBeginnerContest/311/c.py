import io
import sys
_INPUT = """\
7
6 7 2 1 3 4 5
"""
sys.stdin = io.StringIO(_INPUT)

def find_cycle(graph, start):
    visited = set()  # 探索済みのノードを記録
    cycle = []
    stack = [start]  # これから探索するノードを記録（スタック）

    while stack:
        vertex = stack.pop()  # スタックからノードを取り出す
        if vertex not in visited:  # ノードがまだ探索済みでなければ
            visited.add(vertex)  # 探索済みとして記録
            cycle.append(vertex)
            stack.extend(graph[vertex])  # 未探索の隣接ノードをスタックに追加
        else: # ノードが探索済み = cycleを発見
            index = cycle.index(vertex)
            return cycle[index:]

    return []

N = int(input())
edges = list(map(int, input().split()))

# 隣接リストの初期化（空のリストで初期化）
adj_dict = {i+1: [] for i in range(N)}

# 隣接リストの作成
for i in range(N):
    adj_dict[i+1].append(edges[i])


for i in range(N):
    cycle = find_cycle(adj_dict, i+1)
    if cycle:
        print(len(cycle))
        print(*cycle)
        exit(0)

