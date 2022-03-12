from collections import deque

m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]


q = deque()
result = -1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i,j])

while q:
    result +=1
    q_len = len(q)

    for _ in range(q_len):
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    q.append([nx, ny])


for a in range(n):
    for b in range(m):
        if graph[a][b] == 0:
            result = -1 #다 익지 못할 때


print(result)


