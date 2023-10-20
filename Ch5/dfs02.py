graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "E"],
    "D": ["B", "G"],
    "E": ["B", "C", "G"],
    "F": ["G"],
    "G": ["D", "E", "F"],
}


def dfs(g: dict[str, list], v: str, visited: set):
    visited.add(v)
    print(v, end=" ")

    for w in g[v]:
        if w not in visited:
            dfs(g, w, visited)


dfs(graph, "A", set())
