t = int(input())

for test_case in range(1,t+1):
    n, m = map(int,input().split())
    graph = [input() for _ in range(n)]
    res = []
    for i in range(n):
        for j in range(n-m+1):
            if graph[i][j:j+m] == graph[i][j:j+m][::-1]:
                res.append(graph[i][j:j+m])
    
    for i in range(n-m+1):
        for j in range(n):
            col_lst = []
            for k in range(m):
                col_lst.append(graph[i+k][j])
            if col_lst == col_lst[::-1]:
                res.append(''.join(col_lst))

    print(f'#{test_case}', end=' ')
    for i in res[0]:
        print(i,end='') 
    print()