from collections import Counter

t = int(input()) #테스트 수

for _ in range(t):
    n = int(input()) #옷 수
    s = []
    for i in range(n):
        a, b = map(str, input().split())
        s.append(b)
        dic = Counter(s)
        result = 1
        for key in dic:
            result *= dic[key] + 1
        print(result -1)