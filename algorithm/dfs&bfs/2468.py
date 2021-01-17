import sys

sys.setrecursionlimit(10000)
input = lambda: sys.stdin.readline().strip()

w, h, k = map(int, input().split())
cnt = 0
ans = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 그래프
graph = [[0] * w for _ in range(h)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 1


# dfs
def dfs(x, y):
    global cnt
    cnt += 1
    graph[x][y] = 1
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 0:
            dfs(nx, ny)


###그래프 전체 탐색
for q in range(h):
    for p in range(w):
        if graph[q][p] == 0:
            cnt = 0
            dfs(q, p)
            ans.append(cnt)

print(len(ans))
ans = sorted(ans)

for an in ans:
    print(an, end=" ")
