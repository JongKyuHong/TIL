t = int(input())


for test_case in range(1,t+1):
    n,m = map(int,input().split())
    array = [list(input()) for _ in range(n)]
    array2 = list(zip(*array))
    result = []
    for i in range(n):
        for j in range(n-m+1):
            if array[i][j:j+m] == array[i][j:j+m][::-1]:
                result.append(array[i][j:j+m])
    
    for i in range(n-m+1):
        for j in range(n):
            col_lst = []
            for k in range(m):
                col_lst.append(array[i+k][j])
            if col_lst == col_lst[::-1]:
                result.append(''.join(col_lst))
    print(f'#{test_case}',end=' ')
    for i in result[0]:
        print(i,end='')
    print()


