for T in range(int(input())):
    n = int(input()) # 신청서
    graph = [list(map(int, input().split())) for _ in range(n)]
    graph.sort(key=lambda x: x[0], reverse=True)
    target = graph[0][0] # 시작시간이 젤 큰놈
    print(graph)
    res = 1
    for i in range(1,n):
        if graph[i][1] <= target:
            target = graph[i][0]
            res += 1
    
    print(f'#{T+1} {res}')