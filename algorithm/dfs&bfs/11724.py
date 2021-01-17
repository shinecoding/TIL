import sys
sys.setrecursionlimit(10000)
input = lambda: sys.stdin.readline().strip()

def dfs(v):
    visited[v] = True
    for k in range(n+1):
        if not visited[k] and conn[v][k] == 1:
            dfs(k)


n, m = map(int, input().split())
conn = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)
count = 0

for _ in range(m):
    x, y = map(int, input().split())
    conn[x][y]=1
    conn[y][x]=1

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        count +=1

print(count)