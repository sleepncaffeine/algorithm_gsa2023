def dfs(g: list[list], v: int):
    visited = [False] * len(g)
    visited[v] = True
    stack = [v]

    while stack:
        v = stack.pop()
        print(v, end=" ")
        for w in sorted(g[v], reverse=True):
            if not visited[w]:
                visited[w] = True
                stack.append(w)


graph = [
    [],
    [2, 3],
    [1, 3],
    [1, 2, 5, 6],
    [5],
    [3, 4, 7],
    [3, 7],
    [5, 6],
]

dfs(graph, 3)
