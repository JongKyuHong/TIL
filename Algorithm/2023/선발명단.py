import sys
input = sys.stdin.readline

def dfs(rows, value):
    global max_v
    if rows == 11:
        max_v = max(max_v, value)
        return
    for i in range(11):
        if visited[i] or not lst[rows][i]:
            continue
        visited[i] = 1
        dfs(rows+1, value + lst[rows][i])
        visited[i] = 0

C = int(input())
for _ in range(C):
    max_v = 0
    lst = [list(map(int, input().split())) for _ in range(11)]
    visited = [0]*11
    dfs(0, 0)
    print(max_v)
