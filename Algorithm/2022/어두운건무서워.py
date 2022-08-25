import sys
input = sys.stdin.readline

r, c, q = map(int, input().split())
graph = []
for _ in range(r):
    data = list(map(int, input().split()))
    graph.append(data)


sum_arr = [[0 for _ in range(c+1)] for _ in range(r+1)]
for i in range(1, r+1):
    for j in range(1, c+1):
        sum_arr[i][j] = graph[i-1][j-1] + (sum_arr[i-1][j] + sum_arr[i][j-1] - sum_arr[i-1][j-1])

for _ in range(q):
    r1,c1,r2,c2 = map(int, input().split()) # 2 2 4 5라고하면
    1134
    res = sum_arr[r2][c2] - sum_arr[r1-1][c2] - sum_arr[r2][c1-1] + sum_arr[r1-1][c1-1]
    idx = (r2+1-r1) *(c2+1-c1)
    print(idx, res)
    print(res//idx)