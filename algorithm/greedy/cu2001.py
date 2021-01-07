p1 = int(input())
p2 = int(input())
p3 = int(input())
j1 = int(input())
j2 = int(input())

p = [p1, p2, p3]
j = [j1, j2]

minP = (min(p) + min(j))*1.1
print(round(minP,1))