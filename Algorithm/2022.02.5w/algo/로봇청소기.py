delta = ((-1,0),(0,1),(1,0),(0,-1))

def dfs(r,c,d):
    global ans
    dir = d
    for i in range(4):
        dir = (dir+3)%4
        nr = r + delta[dir][0]
        nc = c + delta[dir][1]
        if 0 <= nr < n and 0 <= nc < m and not array[nr][nc]:
            array[nr][nc] = 2
            ans += 1
            dfs(nr,nc,dir)
            return
    nr = r - delta[dir][0]
    nc = c - delta[dir][1]
    if array[nr][nc] == 1:
        return
    else:
        dfs(nr,nc,d)
 
n, m = map(int, input().split())
r, c, d = map(int, input().split())
array =[list(map(int, input().split())) for _ in range(n)]
ans = 1
array[r][c] = 2
dfs(r,c,d)
print(ans)