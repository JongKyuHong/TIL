for _ in range(int(input())):
    array = list(input())
    stack = []
    for i in array:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
    if stack:
        print('NO')
    else:
        print('YES')