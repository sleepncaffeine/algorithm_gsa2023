from collections import deque


def bfs(graph: dict[str, list], start: str):
    visited = set(start)  # 시작 정점 방문 처리
    queue = deque([start])  # 시작 정점을 queue에 넣고 시작

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for w in graph[v]:
            if w not in visited:
                queue.append(w)
                visited.add(w)


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "E"],
    "D": ["B", "G"],
    "E": ["B", "C", "G"],
    "F": ["G"],
    "G": ["D", "E", "F"],
}

bfs(graph, "A")  # A B C D E G F
