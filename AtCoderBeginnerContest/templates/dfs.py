def dfs(graph, start):
    visited = set()  # 探索済みのノードを記録
    stack = [start]  # これから探索するノードを記録（スタック）

    while stack:
        vertex = stack.pop()  # スタックからノードを取り出す
        if vertex not in visited:  # ノードがまだ探索済みでなければ
            visited.add(vertex)  # 探索済みとして記録
            stack.extend(graph[vertex] - visited)  # 未探索の隣接ノードをスタックに追加
    return visited