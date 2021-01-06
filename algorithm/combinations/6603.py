from itertools import combinations

while True:
    data = list(map(int, input().split()))
    if data[0] == 0:
        break;
    del data[0]

    data = list(combinations(data, 6))

    for i in data:
        for j in list(i):
            print(j, end=" ")
        print()
    print()