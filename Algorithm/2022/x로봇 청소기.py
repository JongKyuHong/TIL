from collections import deque

delta = ((0,-1),(1,0),(0,1),(-1,0))
n, m = map(int, input().split())
r,c,d = map(int, input().split())
# d, 0:북쪽, 1:동쪽, 2:남쪽, 3:서쪽
array = [list(map(int, input().split())) for _ in range(n)]
res = 1
visited = [[0]*m for _ in range(n)]
while 1:
    flag = 0
    for _ in range(4):
        nr = r + delta[(d+3)%4][0]
        nc = c + delta[(d+3)%4][1]
        d = (d+3)%4
        if 0 <= nr < n and 0 <= nc < m and not array[nr][nc]:
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                res += 1
                r = nr
                c = nc
                flag = 1
                break
    if flag == 0:
        if array[r-delta[d][0]][c-delta[d][1]] == 1:
            print(res)
            break
        else:
            r,c = r-delta[d][0], c-delta[d][1]