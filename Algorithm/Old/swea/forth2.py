T = int(input())

for test_case in range(1, T + 1):
    array = list(input().split())
    stack = []
    for i in array:
        if i == '.':
            if len(stack) == 1:
                result = stack.pop()
                print(f'#{test_case} {result}')
                break
            else:
                print(f'#{test_case} error')
                break
        if i.isdigit():
            stack.append(int(i))
        elif i == '+':
            if len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)
            else:
                print(f'#{test_case} error')
                break
        elif i == '-':
            if len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            else:
                print(f'#{test_case} error')
                break
        elif i == '/':
            if len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                stack.append(b // a)
            else:
                print(f'#{test_case} error')
                break
        elif i == '*':
            if len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)
            else:
                print(f'#{test_case} error')
                break