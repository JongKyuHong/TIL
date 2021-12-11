for test_case in range(1,11):
    n, number = input().split() # 문자의 총 수, 번호 문자열
    stack = [number[0]]
    for i in range(1,len(number)):
        if stack[-1] == number[i]:
            stack.pop()
        else:
            stack.append(number[i])
    
    print(f'#{test_case}',end=' ')
    for i in stack:
        print(i,end='')
        



