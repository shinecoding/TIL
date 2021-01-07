n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))
total = 0
minP = 0

for i in range(n-1):
    if i == 0:
        total += road[i] * price[i]
        minP = price[i]
    else:
        minP = min(minP, price[i])
        total += road[i] * minP
print(total)