from collections import deque


def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append([0,0])
    graph[0][0] = 1

    distance[0][0] = 1

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and distance[nx][ny] == 0:
                    distance[nx][ny] = distance[x][y] + 1
                    q.append([nx, ny])

    print(distance[n - 1][m - 1])


n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]
distance = [[0] * m for _ in range(n)]

bfs()


