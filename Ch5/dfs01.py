def dfs(g: list[list], v: int, visited: list[bool]):
    visited[v] = True
    print(v, end=" ")

    for w in g[v]:
        if not visited[w]:
            dfs(g, w, visited)


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

dfs(graph, 3, [False] * len(graph))
