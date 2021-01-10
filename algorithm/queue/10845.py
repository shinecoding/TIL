from collections import deque
import sys

queue = deque()


def push(x):
    queue.append(x)


def pop():
    if queue:
        print(queue.popleft())
    else:
        print(-1)

def size():
    print(len(queue))


def empty():
    if not queue:
        print(1)
    else:
        print(0)


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


n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    order = sys.stdin.readline().rstrip().split()
    if order[0] == "push":
        push(order[1])
    elif order[0] == "pop":
        pop()
    elif order[0] == "size":
        size()
    elif order[0] == "empty":
        empty()
    elif order[0] == "front":
        front()
    elif order[0] == "back":
        back()