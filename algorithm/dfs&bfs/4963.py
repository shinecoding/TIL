import sys
input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(1000000)

dx = [-1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]


def dfs(x,y):
    visited[x][y] = 1
    for a in range(8):
        nx = x + dx[a]
        ny = y + dy[a]

        if 0<= nx < h and 0<= ny < w:
            if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                dfs(nx, ny)


while True:
    w, h = map(int, input().split())
    if w==0 and h==0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    count = 0

    for i in range(h):
        for j in range(w):
            if visited[i][j] == 0 and graph[i][j] == 1:
                dfs(i,j)
                count +=1

    print(count)
