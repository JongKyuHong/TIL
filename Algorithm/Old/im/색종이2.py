graph = [[0]*100 for _ in range(100)]
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
for a,b in paper:
    for i in range(b-10, b):
        for j in range(a, a+10):
            graph[i][j] = 1
cnt = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1:
            cnt += 1
print(cnt)
