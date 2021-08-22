t = int(input())

for test_case in range(1,t+1):
    n, k = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(n)]
    res = []
    for i in range(n):
        cnt = 1
        prev = 2
        for j in range(n):
            if prev == 1:
                if graph[i][j] == 1:
                    cnt += 1
                else:
                    res.append(cnt)
                    cnt = 1
                    prev = 0
            elif prev != 1:
                if graph[i][j] == 1:
                    cnt = 1
                    prev = 1
                else:
                    prev = 0
        res.append(cnt)
    for i in range(n):
        cnt = 1
        prev = 2
        for j in range(n):
            if prev == 1:
                if graph[j][i] == 1:
                    cnt += 1
                else:
                    res.append(cnt)
                    cnt = 1
                    prev = 0
            elif prev != 1:
                if graph[j][i] == 1:
                    cnt = 1
                    prev = 1
                else:
                    prev = 0
        res.append(cnt)
    result = res.count(k)
    print(f'#{test_case} {result}')



