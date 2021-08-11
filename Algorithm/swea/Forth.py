t = int(input())

for test_case in range(1,t+1):
    array = list(input().split())
    stack = []
    for i in array:
        if i == '.':  # .을 만났을경우
            if len(stack) == 1:  # 스택에 남아있는 숫자가 하나인경우
                result = stack.pop()
                print(f'#{test_case} {result}')  # 정상출력
                break
            else:  # 스택에 하나만 들어있지 않은경우
                print(f'#{test_case} error')  # 에러 발생
                break
        if i.isdigit():  # 숫자가 들어오면
            stack.append(int(i))  # 스택에 저장
        # 연산자가 들어오면 그에맞는 연산을하고 스택안에 넣는다.
        # 스택의 길이가 2이상이 아니라면 에러발생
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
        
        



