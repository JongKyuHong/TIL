for test_case in range(10):
    tc = int(input())
    number = list(map(int,input().split()))
    i = 0
    while 1:
        if number[0] - (i+1) <= 0:
            number.pop(0)
            number.append(0)
            break
        else:
            number.append(number.pop(0)-(i+1))
        i += 1
        if i == 5:
            i = 0
    print(f'#{tc}',*number)