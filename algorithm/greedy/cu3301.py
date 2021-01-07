n = int(input())
coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
cnt = 0

for coin in coins:
    cnt += n // coin
    n= n%coin

print(cnt)