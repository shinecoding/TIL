a, b = map(int, input().split())
cnt = 0

diff = abs(b -a)

while diff !=0:
    if diff>7:
        diff -= 10
        cnt += 1
        diff = abs(diff)
    elif diff>3:
        diff -= 5
        cnt += 1
        diff = abs(diff)
    elif diff>0:
        diff -= 1
        cnt += 1
        diff = abs(diff)
print(cnt)