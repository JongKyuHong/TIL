from collections import deque
# import sys
# input = sys.stdin.readline

delta = ((0,1),(1,0))
def bfs(r, c):
    global res
    q = [(r,c)]
    q = deque(q)
    while q:
        r, c = q.popleft()
        if r == n-1 and c == n-1:
            res = min(res, visited[r][c])
            continue
        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc]:
                    visited[nr][nc] = visited[r][c] + nums[nr][nc]
                    q.append((nr, nc))
                else:
                    if visited[nr][nc] > visited[r][c] + nums[nr][nc]:
                        visited[nr][nc] = visited[r][c] + nums[nr][nc]
                        q.append((nr, nc))



for T in range(int(input())):
    n = int(input()) # 가로세로 칸
    nums = [list(map(int, input().split())) for _ in range(n)]
    res = float('inf')
    visited = [[0 for i in range(n)] for _ in range(n)]
    visited[0][0] = nums[0][0]
    bfs(0, 0)
    print(f'#{T+1} {res}')