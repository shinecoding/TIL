n = int(input())

m = []

for _ in range(n):
     m.append(int(input()))


    #Insertion Sort
for i in range(1, len(m)):
    while (i>0) & (m[i] < m[i-1]):
        m[i], m[i-1] = m[i-1], m[i]

        i-=1

for k in m:
    print(k)