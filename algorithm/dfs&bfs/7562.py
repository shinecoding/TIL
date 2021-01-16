from collections import deque

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]


def bfs():
    q = deque()
    q.append([s1,s2])
    graph[s1][s2] = 1

    while q:
        x, y = q.popleft()
        if x == e1 and y == e2:
            return graph[x][y] -1

        for step in steps:
            nx = x + step[0]
            ny = y + step[1]
            if 0<=nx<l and 0<=ny<l:
                if graph[nx][ny] == 0:
                    q.append([nx, ny])
                    graph[nx][ny] = graph[x][y]+1


t = int(input()) #테스트 케이스

for _ in range(t):
    l = int(input())
    graph = [[0] * l for _ in range(l)]

    s1, s2 = map(int, input().split())
    e1, e2 = map(int, input().split())
    if s1 == e1 and s2 == e2:
        print(0)
        continue

    ans = bfs()
    print(ans)