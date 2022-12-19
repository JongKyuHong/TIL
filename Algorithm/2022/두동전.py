from collections import deque
import sys
input = sys.stdin.readline
delta = ((0,1),(0,-1),(1,0),(-1,0))
def bfs():
    while coin:
        r1, c1, r2, c2, cnt = coin.popleft()
        if cnt > 10:
            return -1

        for dr, dc in delta:
            nr1, nc1, nr2, nc2 = r1+dr, c1+dc, r2+dr, c2+dc
            if 0 <= nr1 < n and 0 <= nc1 < m and 0 <= nr2 < n and 0 <= nc2 < m:
                if graph[nr1][nc1] == '#':
                    nr1, nc1 = r1, c1
                if graph[nr2][nc2] == '#':
                    nr2, nc2 = r2, c2
                coin.append((nr1,nc1,nr2,nc2,cnt+1))
            elif 0 <= nr1 < n and 0 <= nc1 < m:
                return cnt+1
            elif 0 <= nr2 < n and 0 <= nc2 < m:
                return cnt+1
            else:
                continue
    return -1
if __name__ ==  "__main__":
    n, m = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(n)]
    tmp = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'o':
                tmp.append((i,j))
    coin = deque()
    coin.append((tmp[0][0],tmp[0][1],tmp[1][0],tmp[1][1],0))
    print(bfs())