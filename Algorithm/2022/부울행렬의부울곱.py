import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
graph2 = [list(map(int, input().split())) for _  in range(n)]

cnt = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[i][k] and graph2[k][j]:
                cnt += 1
                break
print(cnt)