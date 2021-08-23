for test_case in range(1,11):
    n = int(input())  # 테스트케이스의 길이
    nums = list(input())
    stack = []
    res = []
    icp = {'*':2, '+':1,'/':2,'-':1}  # 우선순위 지정
    for i in nums:
        if i.isdigit():
            res.append(i)  # 숫자일경우에 res리스트에 바로 넣음
        else:
            while stack:  # 낮은우선순위가 나올때까지 while문 반복
                if icp.get(i) > icp.get(stack[-1]):  # 낮은우선순위가 나오면 while문종료
                    break
                res.append(stack.pop())  # 낮은 우선순위가 나오지않은경우 stack pop
            stack.append(i)
    while stack:  # 혹시 스택에 남은값이 있을경우 res에 모두 넣어준다.
        res.append(stack.pop())
    print(res)
    stack = []
    for i in res:
        if i.isdigit():
            stack.append(i)
        else:
            a = int(stack.pop())
            b = int(stack.pop())
            if i =='*':
                stack.append(b*a)
            else:
                stack.append(b+a)
    print(f'#{test_case}', stack[-1])