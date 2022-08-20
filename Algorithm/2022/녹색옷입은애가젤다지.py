import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize
# 링크가 n-1, n-1까지 이동하는데 잃을 수 밖에없는 최소금액을 구하시오
delta = ((0,1),(0,-1),(1,0),(-1,0))
case_Num = 1
while 1:
    N = int(input()) # 동굴의 크기
    if N == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(N)]
    q = [[graph[0][0],0, 0]]
    cost = [[INF] * N for _ in range(N)]
    cost[0][0] = graph[0][0]
    while q:
        rupee, r, c = heapq.heappop(q)
        if cost[r][c] < rupee:
            continue
        for dr, dc in delta:
            nr = dr + r
            nc = dc + c
            if 0 <= nr < N and 0 <= nc < N:
                d = rupee + graph[nr][nc]
                if cost[nr][nc] > d:
                    cost[nr][nc] = d
                    heapq.heappush(q,(d,nr,nc))
    
    print(f'Problem {case_Num}: {cost[N-1][N-1]}')
    case_Num += 1
        
