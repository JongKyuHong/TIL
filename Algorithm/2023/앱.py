from collections import deque
import sys
input = sys.stdin.readline
delta = ((0,1),(0,-1),(1,0),(-1,0))

def bfs(r, c, start):
    q = deque()
    q.append((r, c))
    visited = [[0]*N for _ in range(N)]
    visited[r][c] = 1
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if [nr, nc] in lst[r][c]:
                    continue
                visited[nr][nc] = 1
                q.append((nr, nc))
    ans = 0
    for i in range(start+1, K):
        r, c = cow[i][0], cow[i][1]
        if not visited[r][c]:
            ans += 1
            
    return ans

N, K, R = map(int, input().split())
graph = [[0]*N for _ in range(N)] # 목초지 격자
lst = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(R):
    r, c, r1, c1 = map(int, input().split())
    lst[r-1][c-1].append([r1-1, c1-1])
    lst[r1-1][c1-1].append([r-1, c-1])
    
cnt = 0
# 길을 건너지 않으면 만날 수 없는 소의 쌍
cow = []
for _ in range(K):
    r, c = map(int, input().split())
    cow.append([r-1, c-1])
for i in range(K):
    # cow[i] # 하나씩 붙잡고 순회?
    cnt += bfs(cow[i][0], cow[i][1], i)
print(cnt)
    

# 내가 지금 하려는거
# 1. 소를 하나씩 잡고 순회함 다른소를 목적지로
# 2. 목적지에 가는 도중에 길을 건넌다면 돌아감
# 3. 도착하지 못한다면 소쌍 += 1