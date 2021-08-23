t = int(input())

for test_case in range(1,t+1):
    n, m = map(int,input().split())
    nums = list(map(int,input().split()))
    maxa = 0
    mina = 10000*100
    for i in range(n-m+1):
        cnt = 0
        for j in range(i,i+m):
            cnt += nums[j]
        maxa = max(maxa,cnt)
        mina = min(mina,cnt)
    res = maxa - mina
    print(f'#{test_case} {res}')




