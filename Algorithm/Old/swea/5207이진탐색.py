def binary_search(arr,target):
    global cnt
    start = 0
    end = len(arr)-1
    flag = 0
    while start <= end:
        mid = (start+end)//2
        if arr[mid] > target:
            end = mid - 1
            if flag == 1: break
            flag = 1
        elif arr[mid] < target:
            start = mid + 1
            if flag == -1: break
            flag = -1
        else:
            cnt += 1
            break



for test_case in range(int(input())):
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    b = list(map(int,input().split()))
    cnt = 0
    for i in b:
        binary_search(a,i)
    print(f'#{test_case+1} {cnt}')






