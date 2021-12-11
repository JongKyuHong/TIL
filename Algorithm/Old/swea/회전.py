for test_case in range(int(input())):
    n, m = map(int,input().split())
    array = list(map(int,input().split()))
    print(f'#{test_case+1} {array[m%n]}')