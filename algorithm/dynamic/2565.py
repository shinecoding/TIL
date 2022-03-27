n = int(input())
lines = []
for _ in range(n):
    a,b = map(int, input().split())
    lines.append((a,b))

lines.sort()


a_to_b = list(map(lambda x: x[1], lines))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if a_to_b[j] < a_to_b[i]:
            dp[i] = max(dp[i], dp[j]+1)

#없애야하는 전깃줄의 최소 개수 = 현재 전깃줄의 개수 - 겹치지 않는 최대 전깃줄의 개수
print(n - max(dp))