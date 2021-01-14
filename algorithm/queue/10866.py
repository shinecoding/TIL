from collections import deque
import sys

def push_front(x):
    queue.appendleft(x)

def push_back(x):
    queue.append(x)

def pop_front():
    if queue:
        print(queue.popleft())
    else:
        print(-1)

def pop_back():
    if queue:
        print(queue.pop())
    else:
        print(-1)

def size():
    print(len(queue))

def empty():
    if queue:
        print(0)
    else:
        print(1)

def front():
    if queue:
        print(queue[0])
    else:
        print(-1)

def back():
    if queue:
        print(queue[-1])
    else:
        print(-1)


n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    order = sys.stdin.readline().split()
    if order[0] == "push_front":
        push_front(order[1])
    elif order[0] == "push_back":
        push_back(order[1])
    elif order[0] == "pop_front":
        pop_front()
    elif order[0] == "pop_back":
        pop_back()
    elif order[0] == "size":
        size()
    elif order[0] == "empty":
        empty()
    elif order[0] == "front":
        front()
    elif order[0] == "back":
        back()
