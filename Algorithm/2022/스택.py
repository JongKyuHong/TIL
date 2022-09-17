stack = []
for _ in range(int(input())):
    data = input().split()
    if data[0] == 'push':
        stack.append(data[1])
    elif data[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif data[0] == 'size':
        print(len(stack))
    elif data[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)