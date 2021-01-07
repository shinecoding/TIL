n = int(input())
s = []

for _ in range(n):
    first, second = map(int, input().split())
    s.append([first, second])

s = sorted(s, key=lambda x: (x[1], x[0]))
endTime = 0
cnt = 0

for i, j in s:
    if i > endTime:
        cnt +=1
        endTime = j
print(cnt)

