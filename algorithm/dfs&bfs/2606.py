from collections import deque


#dfs
def dfs():
    q = deque([1])
    visited[1] = True
    virus = 0
    while q:
        v = q.popleft()

        for i in range(1, 1+num):
            if not visited[i] and graph[v][i] == 1:
                q.append(i)
                visited[i] = True
                virus += 1

    print(virus)


num = int(input())
conn = int(input())
graph = [[0]*(num+1) for _ in range(num + 1)]
visited = [False] * (num+1)

for _ in range(conn):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

dfs()




