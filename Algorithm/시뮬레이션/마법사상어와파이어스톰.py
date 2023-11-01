from collections import deque
import sys 
input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def rotate(arr):
    n, m = len(arr), len(arr[0])
    result = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            result[i][j] = arr[n-1-j][i]
    return result

def devide(storm):
    tmp = 2**storm
    positions = []
    for i in range(0, 2**N, tmp):
        for j in range(0, 2**N, tmp):
            positions.append(((i, j), (i+tmp, j+tmp)))
    return positions

def melt():
    melted = []
    for i in range(2**N):
        for j in range(2**N):
            cnt = 0
            for k in range(4):
                nr = i + dx[k]
                nc = j + dy[k]
                if 0 <= nr < 2**N and 0 <= nc < 2**N:
                    if lst[nr][nc] >= 1:
                        cnt += 1
            if cnt < 3:
                melted.append((i, j))
    return melted

def bfs(r, c):
    global answer2
    q = deque()
    q.append((r, c))
    visited[r][c] = 1
    cnt = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r+dx[i], c+dy[i]
            if 0 <= nr < 2**N and 0 <= nc < 2**N and not visited[nr][nc] and lst[nr][nc] >= 1:
                visited[nr][nc] = 1
                cnt += 1
                q.append((nr, nc))
    answer2 = max(answer2, cnt)    

N, Q = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(2**N)]
firestorm = list(map(int, input().split()))
for storm in firestorm:
    positions = devide(storm)
    for position in positions:
        pos1, pos2 = position
        arr = []
        for i in range(pos1[0], pos2[0]):
            tmp = []
            for j in range(pos1[1], pos2[1]):
                tmp.append(lst[i][j])
            arr.append(tmp)
        arr = rotate(arr)
        step = 2**storm
        for i in range(step):
            for j in range(step):
                lst[i+pos1[0]][j+pos1[1]] = arr[i][j]
    melted = melt()
    for x, y in melted:
        if lst[x][y] >= 1: 
            lst[x][y] -= 1

answer = 0
for row in lst:
    answer += sum(row)
print(answer)

answer2 = 0
visited = [[0]*(2**N) for _ in range(2**N)]
for i in range(2**N):
    for j in range(2**N):
        if not visited[i][j] and lst[i][j] >= 1:
            bfs(i, j)
print(answer2)