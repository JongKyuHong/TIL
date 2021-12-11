for test_case in range(int(input())):
    n, num = input().split()
    ten = int('0x'+num,16)
    b = format(ten,'b')
    print(b)
    if len(b) < int(n)*4:
        b = '0'+b
    print(f'#{test_case+1} {b}')