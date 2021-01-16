from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()


def bfs(x):
    q.append(x)
    visited[x] = 1

    while q:
        x = q.popleft()
        for nx in graph[x]:
            if visited[nx] == 0: #방문 안 한 곳
                visited[nx] = -1 * visited[x] #다음단계 전부 마이너스로 색상반전
                q.append(nx)
            elif visited[nx] == visited[x]: #색이 같으면
                return 1
    return 0


k = int(input()) #테스트 케이스
for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v)]
    visited = [0 for _ in range(v)]
    q = deque()
    for _ in range(e):
        v1, v2 = map(int, input().split())
        graph[v1-1].append(v2-1)
        graph[v2-1].append(v1-1)
    ans = 0
    for i in range(v):
        if visited[i] == 0:
            ans = bfs(i)
            if ans == 1:
                break
    if ans == 0:
        print("YES")
    else:
        print("NO")