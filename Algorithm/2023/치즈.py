from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
delta = ((0,1),(0,-1),(1,0),(-1,0))

# 1플랜
# 0을기준으로 bfs를 돌림 근데 이게 치즈 구멍이 아니라고 판단할 필요가 있다. 
# 0인애들은 visited모두 1으로 계속 둠

ans = 0
prev = 0
while 1:
    q = deque()
    q.append((0, 0))
    visited = [[0]*M for _ in range(N)]
    visited[0][0] = 1
    cnt = 0
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc]:
                    if lst[nr][nc] == 0:
                        q.append((nr, nc))
                    else: # 지워야 하는 대상
                        cnt += 1
                        lst[nr][nc] = 0
                    visited[nr][nc] = 1
    if cnt == 0:
        print(ans)
        print(prev)
        break
    else:
        prev = cnt
        ans += 1