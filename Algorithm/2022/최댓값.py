import sys 
input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(9)]
answer = -1
r, c = 0, 0
for i in range(9):
    for j in range(9):
        if answer < graph[i][j]:
            answer = graph[i][j]
            r, c = i, j
print(answer)
print(r+1, c+1)