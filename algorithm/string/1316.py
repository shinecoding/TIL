n = int(input())
cnt = 0

for i in range(n):
    word = input()
    if list(word) == sorted(word, key=word.find):
        cnt +=1
print(cnt)


#sorted에서 key=word.find 로 설정하면 "a"부터 정렬되는 것이 아니라, word에서 찾아지는 character 순서대로 정렬된다.

