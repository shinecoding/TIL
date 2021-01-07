n = int(input())  # 토핑종류n
d_price, t_price = map(int, input().split())  # 도우가격a, 토핑가격b
d_cal = int(input())  # 도우 칼로리c
t_cal = []  # 토핑 칼로리 리스트
for i in range(n):
    t_cal.append(int(input()))

# 토핑 칼로리 내림차순
t_cal.sort(reverse=True)

# 도우만 있을 경우
minCal = d_cal // d_price  # 도우칼로리/도우가격

# 칼로리가 큰순으로 비교
for k in t_cal:
    d_price += t_price  # 도우가격+토핑가격
    if (d_cal + k) / d_price > minCal:
        d_cal += k
        minCal = d_cal // d_price
    else:
        break
print(int(minCal))