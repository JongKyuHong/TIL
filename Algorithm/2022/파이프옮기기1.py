import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 0
def dfs(r, c, dir):
    global ans
    if r == n-1 and c == n-1:
        ans += 1
        return
    if dir == 0:
        if c+1 < n and not graph[r][c+1]:
            dfs(r, c+1, 0)
        if r+1 < n and c+1 < n and not graph[r][c+1] and not graph[r+1][c] and not graph[r+1][c+1]:
            dfs(r+1, c+1, 2)
    elif dir == 1:
        if r+1 < n and not graph[r+1][c]:
            dfs(r+1, c, 1)
        if r+1 < n and c+1 < n and not graph[r][c+1] and not graph[r+1][c] and not graph[r+1][c+1]:
            dfs(r+1, c+1, 2)
    else:
        if c+1 < n and not graph[r][c+1]:
            dfs(r, c+1, 0)
        if r+1 < n and not graph[r+1][c]:
            dfs(r+1, c, 1)
        if r+1 < n and c+1 < n and not graph[r][c+1] and not graph[r+1][c] and not graph[r+1][c+1]:
            dfs(r+1, c+1, 2)

# dir 0은 가로 1은 세로 2는 대각선
dfs(0, 1, 0)
print(ans)