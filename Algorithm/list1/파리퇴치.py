t = int(input())

for test_case in range(1,t+1):
    n, m = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    maxa = 0
    for i in range(n-m):
        for j in range(n-m):
            cnt = 0
            for x in range(m):
                for y in range(m):
                    cnt += matrix[i+x][j+y]
            maxa = max(maxa,cnt)
    print(f'#{test_case} {maxa}')      




