for test_case in range(int(input())):
    n, m = map(int,input().split())
    graph = [input() for _ in range(n)]
    res = []
    for i in range(n):
        for k in range(n-m+1):
            if graph[i][k:k+m] == graph[i][k:k+m][::-1]:
                res.append(graph[i][k:k+m])
                break
    
    for i in range(n):
        for j in range(n-m+1):
            lst = ''
            for k in range(m):
                lst += graph[j+k][i]
            if lst == lst[::-1]:
                res.append(lst)
                break
    res = res[-1]
    print(f'#{test_case+1} {res}')

