n = int(input())

for _ in range(n):

    m = list(input())
    sum = 0
    num = 0

    for i in m:
        if i == "O":
            num +=1
            sum += num
        else:
            num = 0

    print(sum)