t = int(input())

for test_case in range(1,t+1):
    n = int(input())
    array = []
    for _ in range(n):
        array.append(list(map(int,input().split())))
    cnt = 0
    for i in range(n):
        for j in range(n):
            if j-1 >= 0:
                cnt += abs(array[i][j] - array[i][j-1])
            if i-1 >= 0:
                cnt += abs(array[i][j] - array[i-1][j])
            if j+1<=n-1:
                cnt += abs(array[i][j] - array[i][j+1])
            if i+1<=n-1:
                cnt += abs(array[i+1][j] - array[i][j])
    print(f'#{test_case} {cnt}')




