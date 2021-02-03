n = input()

length = len(n)

for start in range(0, length, 10):
    enter = start + 10
    print(n[start:enter])