def change_bin(n):
    a = 1
    answer =''
    cnt = 0
    while n:
        if n < 2**-a:
            answer += '0'
        else:
            n -= 2**-a
            answer += '1'
        cnt += 1
        if cnt > 12:
            return 'overflow'
        else:
            a += 1
    return answer


for test_case in range(int(input())):
    n = float(input())
    print(f'#{test_case+1} {change_bin(n)}')