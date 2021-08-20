t = int(input())

for test_case in range(1,t+1):
    n = int(input())
    color_list = [list(map(int,input().split()))for _ in range(n)]
    graph = [['0']* 10 for _ in range(10)]
    for k in range(n):
        r1,c1,r2,c2,color = color_list.pop(0)
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                graph[i][j] += str(color)
    res = 0
    for i in graph:
        for j in i:
            if '1' in j and '2' in j:
                res += 1
    print(f'#{test_case} {res}')







