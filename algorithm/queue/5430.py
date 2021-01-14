import sys
from collections import deque
t = int(sys.stdin.readline()) #테스트케이스 수

for _ in range(t):
    p = sys.stdin.readline().strip() #스트링
    n = int(sys.stdin.readline()) #배열에 들어갈 수
    #덱에 입력받아서 넣기
    line = sys.stdin.readline()[1:-2].split(",")
    q = deque()
    for each in line:
        if each != '':
            q.append(each)

    errorflag = 0
    reverse = 0

    #명령어 하나씩
    for letter in p:
        if letter == "R": #리버스
            if reverse == 0:
                reverse = 1
            else:
                reverse = 0
        else: #D 면 리버스 방향에 따라 앞이나 뒤 삭제
            if q and q[0] != '':
                if reverse == 0:
                    q.popleft()
                else:
                    q.pop()
            else:
                errorflag = 1
                break
    if errorflag == 1: #에러남
        print("error")
    else:
        if reverse == 1: #리버스
            q.reverse()
        print("[", end="")
        for i in range(len(q)):
            if i == len(q)-1:
                print(str(q[i]), end="")
            else:
                print(q[i], end=",")
        print("]")