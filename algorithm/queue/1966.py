from collections import deque

queue = deque()

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    for _ in range(n):
        queue.append(map(int, input().split()))

    for k in range(n):
        for i in range(1, n):
            if queue[0] < queue[i]:
                queue.append(queue.popleft())
            else:
                print(queue.popleft(), end=" ")