from collections import deque

delta = ((0,1),(0,-1),(1,0),(-1,0))
for test_case in range(int(input())):
    n = int(input())
    INF = float('inf')
    graph = [list(map(int, input().split())) for _ in range(n)]
    q = []
    q = deque()
    q.append((graph[0][0], 0, 0))
    distance = [[INF]*n for _ in range(n)]
    while q:
        dist, r, c = q.popleft()
        if distance[r][c] < dist:
            continue
        for dr, dc in delta:
            nr = r+dr
            nc = c+dc
            if 0 <= nr < n and 0 <= nc < n:
                cost = dist + graph[nr][nc]
                if cost < distance[nr][nc]:
                    distance[nr][nc] = cost
                    q.append((cost,nr,nc))
    print(distance[n-1][n-1])
    
    