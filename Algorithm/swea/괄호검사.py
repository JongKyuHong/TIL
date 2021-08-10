t = int(input())

for test_case in range(1,t+1):
    text = list(input())
    stack = []  # 괄호만을 담을 스택
    flag = 0
    for i in text: 
        if i == '(' or i=='{':  # 여는 괄호일때 스택안에 넣는다.
            stack.append(i)
        elif i == ')':  # 닫는 소괄호가 나오면 스택을 pop하고 여는 소괄호가 나온다면 넘어가고
            if stack:
                a = stack.pop()
                if a == '{':  # 여는 중괄호가 나올시에 제대로 닫혀있지 않은것이므로
                    print(f'#{test_case} 0')  # 0을 출력한다.
                    flag = 1  # 여기서 걸리지않고 스택이 남아있거나 괄호가 짝이 안맞는경우를 걸러내기위한 flag값
                    break
            else:
                print(f'#{test_case} 0')
                flag = 1
                break
        elif i=='}':
            if stack:
                a = stack.pop()
                if a == '(':
                    print(f'#{test_case} 0')
                    flag = 1
                    break
            else:
                print(f'#{test_case} 0')
                flag = 1
                break
    if flag == 0:
        if stack:
            print(f'#{test_case} 0')
        else:
            print(f'#{test_case} 1')





