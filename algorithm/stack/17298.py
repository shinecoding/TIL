n = int(input())

arr = list(map(int, input().split()))
stack = []
ans = [-1 for _ in range(n)]

for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        ans[stack[-1]] = arr[i]
        print(stack[-1])
        stack.pop()
        print(" i="+ str(i) + " ans="+ str(arr[i]))
    stack.append(i)
    print("append="+str(i))
for i in range(n):
    print(ans[i], end=" ")

