graph = [[0 for _ in range(101)] for _ in range(101)]
for i in range(4):
    a1, b1, a2, b2 = map(int,input().split())
    for i in range(b1,b2):
        for j in range(a1,a2):
            print(graph[i][j],' 전')
            graph[i][j] = 1
            print(graph[i][j],' 후')
cnt = 0
for i in graph:
    for j in i:
        if j == 1:
            cnt += 1
print(cnt)




