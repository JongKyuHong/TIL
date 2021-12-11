for test_case in range(int(input())):
    n = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    list = [0] * 8
    for i in range(8):
        if n//money[i] != 0:
            list[i] = n//money[i]
            n %= money[i]
    print(f'#{test_case+1}')
    print(*list)

