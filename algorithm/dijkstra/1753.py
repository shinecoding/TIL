import heapq

INF = int(1e9)

#노드의 개수, 간선의 개수
n, m = map(int, input().split())
#시작 노드
start = int(input())
#노드 연결 정보
graph = [[] for i in range(n+1)]
#최단거리 테이블
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

print(graph)

def dijkstra(start):
    q = []
    #시작 노드로 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for near in graph[now]:
            cost = dist + near[1]
            if cost < distance[near[0]]:
                distance[near[0]] = cost
                heapq.heappush(q, (cost, near[0]))


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")

    else:
        print(distance[i])