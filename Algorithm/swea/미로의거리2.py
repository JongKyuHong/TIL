from collections import deque


def bfs(y, x):
    maze[y][x] = 1
    que = deque([[y,x]])
    while que:
        y, x = que.popleft()
        for dy,dx in direction:
            ny = dy+y
            nx = dx+x
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
    distance = [[0 for i in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                start_x = j
                start_y = i
            elif maze[i][j] == 3:
                destination_x = j
                destination_y = i
    bfs(start_y, start_x)
    print(f'#{test_case+1} {distance[destination_y][destination_x]}')




