t = int(input())

for test_case in range(1,t+1):
    n,m = map(int,input().split())
    array = [list(map(int,input().split())) for _ in range(n)]
    maxa = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            cnt = 0
            for k in range(i,i+m):
                for l in range(j,j+m):
                    cnt += array[k][l]
            maxa = max(maxa,cnt)
    print(f'#{test_case} {maxa}')