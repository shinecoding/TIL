n, k = map(int, input().split())  # 동전 종류n, 합k
count = 0  # 총갯수
coins = [int(input()) for _ in range(n)]

for i in range(1, n + 1):
    coin = coins[-i]
    if k >= coin:
        count += k // coin  # 나눔
        k %= coin  # 나눈 나머지값

print(count)