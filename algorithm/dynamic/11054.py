n = int(input())

a = list(map(int, input().split()))
r = a[::-1]

dp = [1] * n
dpr = [1] * n
print(a)
print(r)

for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            #전꺼 < #현재꺼
            dp[i] = max(dp[i], dp[j]+1)

        if r[j] < r[i]:
            dpr[i] = max(dpr[i], dpr[j]+1)

print(dp)
print(dpr)

answer = [0] * n

for i in range(n):
    answer[i] = dp[i] + dpr[n-i-1] -1
    #예시의 경우, 1,2,3,4,5 / 5,2,1 총 길이 8에서 중복된 5를 한번 빼주면 7이 나온다.
print(answer)
print(max(answer))
