t = int(input())

for test_case in range(1,t+1):
    n = int(input())
    array = [[1]*x for x in range(1,n+1)]
    for i in range(2,n):
        for j in range(i):
            if j != i and j!=0:
                array[i][j] = array[i-1][j-1] + array[i-1][j]
    print(f'#{test_case}')
    for i in array:
        print(*i)