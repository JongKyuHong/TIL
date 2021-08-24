for tc in range(1,11):
    n = int(input())
    array = input()
    stack = []
    res = []
    isp = {'(':0,'+':1,'*':2}
    icp = {'(':3,'+':1,'*':2}
    for i in range(n):
        if array[i].isdigit():
            res.append(array[i])
        elif array[i] == ')':
            while stack and stack[-1] != '(':
                res.append(stack.pop())
            stack.pop()
        else:
            while stack and isp[stack[-1]] > icp[array[i]]:
                res.append(stack.pop())
            stack.append(array[i])
    while stack:  # 혹시 스택에 남은값이 있을경우 res에 모두 넣어준다.
        res.append(stack.pop())
    stack = []
    for i in res:
        if i.isdigit():
            stack.append(i)
        else:
            a = int(stack.pop())
            b = int(stack.pop())
            if i == '+':
                stack.append(b+a)
            else:
                stack.append(b*a)
    print(f'#{tc}', *stack)