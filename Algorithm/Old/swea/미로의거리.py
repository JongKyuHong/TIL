from collections import deque


def bfs(y,x):
    que = deque([[y,x]])
    while que:
        y, x = que.popleft()
        for dy, dx in direction:
            nx = x + dx
            ny = y + dy
            if (0 <= nx < n) and (0 <= ny < n) and maze[ny][nx] != 1:
                if maze[ny][nx] == 3:
                    distance[ny][nx] = distance[y][x]
                    return
                maze[ny][nx] = 1
                distance[ny][nx] = distance[y][x] + 1
                que.append([ny, nx])


direction = ((1,0),(-1,0),(0,1),(0,-1))


for test_case in range(int(input())):
    n = int(input())  
    maze = [list(map(int,input())) for _ in range(n)]
    distance = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                x = j
                y = i
            elif maze[i][j] == 3:
                goal_x = j
                goal_y = i
    bfs(y,x)
    print(f'#{test_case+1} {distance[goal_y][goal_x]}')