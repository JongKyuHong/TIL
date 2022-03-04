from collections import deque
delta = ((0,-1),(0,1),(1,0),(-1,0))


def solution(dirs):
    global res
    bfs(5,5,dirs)
    return res+1

def bfs(r,c,dirs):
    global res
    visited[r][c] = 1
    q = deque()
    q.append((r,c))
    i = 0
    while q:
        r, c = q.popleft()
        if dirs[i] == "L":
            nr = r + delta[0][0]
            nc = c + delta[0][1]
        elif dirs[i] == 'R':
            nr = r + delta[1][0]
            nc = c + delta[1][1]
        elif dirs[i] == 'U':
            nr = r + delta[2][0]
            nc = c + delta[2][1]
        else:
            nr = r + delta[3][0]
            nc = c + delta[3][1]
        if 0 <= nr < 11 and 0 <= nc < 11 and not visited[nr][nc]:
            res += 1
            visited[nr][nc] = 1
            q.append((nr,nc))
        i+=1
            
        
array = [[0]*11 for _ in range(11)]
array[5][5] = 1
visited = [[0]*11 for _ in range(11)]
res = 0
n = list(input())
print(solution(n))