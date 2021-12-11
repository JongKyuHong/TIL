t = int(input())
for test_case in range(1,t+1):
    n,m = map(int,input().split())
    ai = list(map(int,input().split()))
    maxa = 0
    mina = 10000*100
    for i in range(len(ai)-m+1):
        cnt = 0
        for j in range(m):
            cnt += ai[i+j]
        maxa = max(maxa,cnt)
        mina = min(mina,cnt)
    print(maxa)
    print(mina)
    print(f'#{test_case} {maxa-mina}')
    


