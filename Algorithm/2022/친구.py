import sys
input = sys.stdin.readline

n = int(input())
graph = [[0]*n for _ in range(n)]
for i in range(n):
    data = input()
    for j in range(n):
        if data[j] == 'N':
            graph[i][j] = 0
            graph[j][i] = 0
        else:
            graph[i][j] = 1
            graph[j][i] = 1
res = 0

for i in range(n):
    cnt = 0
    for j in range(n):
        if graph[i][j] == 1:
            #print(i, j, 'ij')
            cnt += 1
        else:
            if i == j:
                continue
            for k in range(n):
                if graph[i][k] and graph[k][j]:
                    #print(i, j, k,'ijk')
                    cnt += 1
                    break
    res = max(res, cnt)
print(res)

