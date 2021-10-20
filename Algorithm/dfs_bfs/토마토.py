from collections import deque
delta = ((0,1),(0,-1),(1,0),(-1,0))

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(m)]
q = deque()
for i in range(m):
    for j in range(n):
        if array[i][j] == 1:
           q.append((i,j))

while q:
    r, c = q.popleft()
    print(array)
    for dr, dc in delta:
        nr, nc = dr + r, dc + c
        # if 0 <= nr < m and 0 <= nc < n and array[nr][nc] == 0:
        #     q.append((nr,nc))
        #     array[nr][nc] = array[r][c] + 1
        if nr < 0 or nc < 0 or nr >= m or nc >= n:
            continue
        if array[nr][nc] == 0:
            array[nr][nc] = array[r][c] + 1
            q.append((nr,nc))
            

ans = 0
for i in array:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    ans = max(ans,max(i))
print(ans-1)
        



