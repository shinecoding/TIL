a = int(input())
b = int(input())
c = int(input())

num = list(str(a*b*c))
zero = 0
cnt = []

for j in range(10):
    print(num.count(str(j)))