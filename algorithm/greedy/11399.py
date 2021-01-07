n = int(input())
time = list(map(int, input().split()))

time.sort()
addd = 0
total = 0

for i in time:
    addd += i
    total += addd
print(total)