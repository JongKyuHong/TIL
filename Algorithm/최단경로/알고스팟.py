import heapq

m, n = map(int, input().split())
maze = [list(input()) for _ in range(n)]
INF = int(1e9)
distance = [[INF] * (m) for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dijkstra(x,y):
    q = []
    heapq.heappush(q,(0,x,y))
    while q:
        dist, x1, y1 = heapq.heappop(q)
        if distance[y1][x1] < dist:
            continue
        for j in range(4):
            nx = dx[j] + x1
            ny = dy[j] + y1
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            else:
                if maze[ny][nx] == '1':
                    cost = dist + 1
                else:
                    cost = dist
                if distance[ny][nx] > cost:
                    distance[ny][nx] = cost
                    heapq.heappush(q,(cost,nx,ny))

dijkstra(0,0)
if maze[n-1][m-1] == '1':
    print(distance[n-1][m-1]+1)
else:
    print(distance[n-1][m-1])
