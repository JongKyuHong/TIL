t = int(input())

for test_case in range(1,t+1):
    n,m = map(int,input().split())
    array = list(map(int,input().split()))
    a, b, cnt = 0, 10**9, 0 # 최대, 최소, 결과값
    
    for i in range(0,n-m+1):
        a1 = 0
        b1 = 0
        for j in range(i,i+m):
            a1 += array[j]
            b1 += array[j]
        a = max(a,a1)
        b = min(b,b1)
    print(a)
    print(b)
    cnt = a-b
    print(f'#{test_case} {cnt}')

