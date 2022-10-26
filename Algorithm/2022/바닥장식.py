import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            answer += 1
            if graph[i][j] == '-':
                idx = j
                while idx < m and graph[i][idx] == '-':
                    visited[i][idx] = 1
                    idx += 1
            else:
                idx = i
                while idx < n and graph[idx][j] == '|':
                    visited[idx][j] = 1
                    idx += 1
print(answer)
