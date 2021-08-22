t = int(input())

for test_case in range(1,t+1):
    array = input()
    array = array.replace('()','-')
    print(array)
    res = 0
    cnt = 0
    for i in array:
        if i == '-':
            res += cnt
        elif i == '(':
            cnt += 1
        elif i == ')':
            res += 1
            cnt -= 1
        print(cnt, res)
    print(f'#{test_case} {res}')



