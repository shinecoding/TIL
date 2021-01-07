n = input().split("-")

sum = 0
for i in n[0].split("+"):
    sum += int(i)

for k in n[1:]:
    for j in k.split("+"):
        sum -= int(j)
print(sum)
