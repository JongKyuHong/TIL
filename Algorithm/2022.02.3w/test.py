from collections import deque

n = int(input())
a = [list(map(int, input())) for _ in range(n)]
ch = [[-1]*n for _ in range(n)]

delta = ((0,1),(0,-1),(1,0),(-1,0))

def bfs():
    q = deque()
    q.append((0,0))
    ch[0][0] = 0
    
    while q:
        r, c = q.popleft()
        for dr,dc in delta:
            nr = dr + r
            nc = dc + c
            if 0 <= nr < n and 0 <= nc < n:
                if ch[nr][nc] == -1:
                    if a[nr][nc] == 0:
                        ch[nr][nc] = ch[r][c] + 1
                        q.append((nr,nc))
                    else:
                        ch[nr][nc] = ch[r][c]
                        q.appendleft((nr,nc))
bfs()
print(ch[n-1][n-1])