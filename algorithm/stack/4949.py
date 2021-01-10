while True:
    a = input()
    if a == '.':
        break
    stack = []
    flag = True

    for i in a:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] == '[':
                flag = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] == '(':
                flag = False
                break
            elif stack[-1] == '[':
                stack.pop()
    if flag == True and not stack:
        print('yes')
    else:
        print('no')


