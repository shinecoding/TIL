n = int(input())
graph = [[int(i) for i in str(input())] for _ in range(n)]
cnt = 0
apt=[]
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x,y):
    global cnt
    graph[x][y] = 0
    cnt+=1

    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]

        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] == 1:
                dfs(nx, ny)


for a in range(n):
    for b in range(n):
        if graph[a][b] == 1:
            cnt = 0
            dfs(a,b)
            apt.append(cnt)

print(len(apt))
apt.sort()
for k in apt:
    print(k)