import sys


def push(x):
    stack.append(x)


def pop():
    return stack.pop() if stack else -1


def size():
    return len(stack)


def empty():
    return 0 if stack else 1


def top():
    return stack[-1] if stack else -1


n = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(n):
    order = sys.stdin.readline().rstrip().split()

    if order[0] == "push":
        push(order[1])
    elif order[0] == "pop":
        print(pop())
    elif order[0] == "size":
        print(size())
    elif order[0] == "empty":
        print(empty())
    elif order[0] == "top":
        print(top())
