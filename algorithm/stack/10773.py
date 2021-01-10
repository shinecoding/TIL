import sys

k = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(k):
    input_num = int(sys.stdin.readline().rstrip())
    if input_num == 0:
        stack.pop()
    else:
        stack.append(input_num)

print(sum(stack))