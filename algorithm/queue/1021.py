import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))

q = deque(range(1, n+1))

total = 0


for i in range(m):
    if nums[i] == q[0]:
        q.popleft()
        continue
    q_idx = q.index(nums[i])

    #뒤>앞으로 옮기는게 이득인 경우   양수:오른쪽이동
    if q_idx > len(q)//2:
        q.rotate(len(q) - q_idx)
        total += (len(q) - q_idx)

    #앞>뒤로 옮기는 게 이득인 경우    음수: 왼쪽이동
    elif q_idx <= len(q)//2:
        q.rotate(-q_idx)
        total += q_idx
    q.popleft()

print(total)