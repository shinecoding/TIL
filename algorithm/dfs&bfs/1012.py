import sys
sys.setrecursionlimit(50000)
t = int(input())
cnt = 0
worm = []
#상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(y,x):
    global cnt
    graph[y][x] = 0
    cnt +=1

    for p in range(4):
        nx = x+ dx[p]
        ny = y+ dy[p]

        if 0<=nx<w and 0<=ny<h:
            if graph[ny][nx] == 1:
                dfs(ny,nx)


for _ in range(t):
    w, h, k = map(int, input().split())
    graph = [[0]*w for _ in range(h)]
    worm = []
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for a in range(h):
        for b in range(w):
            if graph[a][b] ==1:
                cnt = 0
                dfs(a,b)
                worm.append(cnt)
    print(len(worm))


