import sys
input = sys.stdin.readline

h, w = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(h)]
answer = [[0]*w for _ in range(h)]

for i in range(h):
    t = -1
    for j in range(w):
        if graph[i][j] == 'c':
            answer[i][j] = 0
            t = j
        else:
            if t == -1:
                answer[i][j] = -1
            else:
                answer[i][j] = (j-t)
for i in answer:
    print(*i)