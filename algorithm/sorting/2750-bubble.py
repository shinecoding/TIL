n = int(input())

m = []

for _ in range(n):
    m.append(int(input()))

    #Bubble Sort
for i in range(len(m)):
    for j in range(len(m)):
        if m[i] < m[j]:
            m[i], m[j] = m[j], m[i]

for k in m:
    print(k)