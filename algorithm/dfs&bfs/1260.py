from collections import deque


def dfs(s):

    visited[s] = True
    print(s, end=" ")

    for j in range(1, n+1):
        if not visited[j] and graph[s][j] == 1:
            dfs(j)

def bfs(s):
    q = deque([s])
    visited[s] = False
    while q:
        s = q.popleft()
        print(s, end=" ")

        for k in range(1, n+1):
            if visited[k] and graph[s][k] == 1:
                q.append(k)
                visited[k] = False



n, m, start = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)
for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

dfs(start)
print()
bfs(start)
