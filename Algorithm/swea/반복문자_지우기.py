t = int(input())

for test_case in range(1,t+1):
    text = list(input())
    stack = []
    for i in text:
        if not stack:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    print(f'#{test_case}',len(stack))