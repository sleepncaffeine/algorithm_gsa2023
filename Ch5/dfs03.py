def dfs(g: list[list], v: int):
    visited = [False] * len(g)
    visited[v] = True
    print(v, end=" ")
    stack = [v]

    while stack:
        has_unvisited = False
        for w in g[stack[-1]]:
            if not visited[w]:
                visited[w] = True
                print(w, end=" ")
                stack.append(w)
                has_unvisited = True
                break

        if not has_unvisited:
            stack.pop()


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
