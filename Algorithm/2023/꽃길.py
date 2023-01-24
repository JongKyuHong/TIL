import sys
input = sys.stdin.readline

delta = ((0,1),(0,-1),(1,0),(-1,0))

def check(r, c, visited):
    for dr, dc in delta:
        nr, nc = dr+r, dc+c
        if (nr, nc) in visited:
            return 0
    return 1

def dfs(visited, total):
    global answer
    if total >= answer:
        return
    if len(visited) == 15:
        answer = min(answer, total)
    else:
        for i in range(1, N-1):
            for j in range(1, N-1):
                if check(i, j, visited) and (i, j) not in visited:
                    tmp = [(i, j)]
                    tmp_cost = graph[i][j]
                    for dr, dc in delta:
                        nr, nc = dr+i, dc+j
                        tmp.append((nr,nc))
                        tmp_cost += graph[nr][nc]
                    dfs(visited+tmp, total+tmp_cost)


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
answer = float('inf')
dfs([], 0)
print(answer)