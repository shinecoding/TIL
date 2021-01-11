from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split()) #문서의 개수, 몇번째로 인쇄되었는지 궁금한 문서가 현재 큐에서 몇번째에 놓여있는지
    queue= deque( map(int, input().split())) #중요도
    cnt = 0 #원하는것:문서가 몇번째로 출력되었는지
    while queue:
        top = max(queue)
        pop = queue.popleft()
        m -= 1
        if top!= pop:
            queue.append(pop)
            if m < 0:
                m = len(queue)-1
        else:
            cnt+=1
            if m == -1:
                print(cnt)
                break