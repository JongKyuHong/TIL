import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().split()) for _ in range(n)]

max_r = 0
r = 0
for i in range(n): # 행 검사기
    r_value = 0
    for j in range(m):
        target = str(graph[i][j])
        for t in target:
            if t == '9':
                r_value += 1
    if max_r < r_value:
        r = i
        max_r = r_value

max_c = 0
c = 0
for i in range(m):
    c_value = 0
    for j in range(n):
        target = str(graph[j][i])
        for t in target:
            if t == '9':
                c_value += 1
    if max_c < c_value:
        c = i
        max_c = c_value

if max_c >= max_r:
    for i in range(n):
        graph[i][c] = 0
else:
    for i in range(m):
        graph[r][i] = 0

res = 0
for i in range(n):
    for j in range(m):
        target = str(graph[i][j])
        for t in target:
            if t == '9':
                res += 1

print(res)
