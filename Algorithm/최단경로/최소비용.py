from collections import deque

for test_case in range(int(input())):
    N = int(input())
    delta = ((1,0), (0,1), (-1,0), (0,-1))
    INF = float('inf')
    array = [list(map(int, input().split())) for _ in range(N)]
    distance = [[INF]*N for _ in range(N)]
    distance[0][0] = 0
    q = deque()
    q.append((0,0))
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            nx, ny = x+dx, y+dy
            if 0 <= ny < N and 0 <= nx < N:
                dist = 1
                if array[nx][ny] > array[x][y]:
                    dist += array[nx][ny] - array[x][y]
                if distance[nx][ny] > distance[x][y] + dist:
                    distance[nx][ny] = distance[x][y] + dist
                    q.append((nx, ny))
    print(f'#{test_case+1} {distance[n-1][n-1]}')
        