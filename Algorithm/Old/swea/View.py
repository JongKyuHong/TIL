t = int(input())

for test_case in range(1,t+1):
    n = int(input())
    array = list(map(int,input().split()))
    cnt = 0
    for i in range(2,n-2):
        if array[i] > array[i-1] and array[i] > array[i-2]:
            if array[i] > array[i+1] and array[i] > array[i+2]:
                cnt += min(array[i]-array[i-1],array[i]-array[i-2],array[i]-array[i+1],array[i]-array[i+2])
    print(f'#{test_case} {cnt}')
