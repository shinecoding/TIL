#l 개의 알파벳
#모음 1개 이상
#자음 2개 이상
#sort asc
#c개의 문자 종류 중
from itertools import combinations

vowels = ['a', 'e','i','o','u']

l, c = map(int, input().split())
pw = sorted(list(map(str, input().split())))

comb = combinations(pw, l)

for i in comb:
    count = 0
    for letter in i:
        if letter in vowels:
            count +=1
    if 1<=count<=l-2:
        print(''.join(i))
