from collections import deque

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

m,n,h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

q = deque()
result = -1

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append([i,j,k])


def bfs():
    while q:
        global result
        result += 1
        q_len = len(q)

        for _ in range(q_len):
            z,y,x = q.popleft()

            for a in range(6):
                nx = x + dx[a]
                ny = y + dy[a]
                nz = z + dz[a]

                if 0<= nx < m and 0<= ny < n and 0<= nz < h:
                    if graph[nz][ny][nx] == 0:
                        graph[nz][ny][nx] = 1
                        q.append([nz, ny, nx])


bfs()

for b in range(h):
    for c in range(n):
        for d in range(m):
            if graph[b][c][d] == 0:
                result = -1

print(result)


