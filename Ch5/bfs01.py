from collections import deque


def bfs(graph, start):
    visited = [False] * len(graph)  # 방문 리스트 초기화
    visited[start] = True  # 시작 정점 방문 처리
    queue = deque([start])  # 시작 정점을 queue에 넣음.

    # queue가 빌 때 까지 반복
    while queue:
        v = queue.popleft()  # 큐에서 정점 하나 꺼낸다.
        print(v, end=" ")  # 꺼낸 정점 출력

        # 해당 정점과 연결된, 아직 방문하지 않은 정점들을 큐에 삽입
        for w in graph[v]:
            if not visited[w]:
                queue.append(w)
                visited[w] = True  # 인접 정점 w 방문 처리


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

bfs(graph, 3)  # 3 1 2 5 6 4 7
