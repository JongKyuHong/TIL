from collections import deque
import sys
input = sys.stdin.readline

def find(r, c):
    q = deque()
    q.append((r,c))
    visited = [[0]*101 for _ in range(101)]
    cluster = [[r,c]]
    visited[r][c] = 1
    while q:
        r, c = q.popleft()
        if r == R-1:
            return 0 # 바닥에 닿아있다.
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < R and 0 <= nc < C and caven[nr][nc] == 'x' and not visited[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr, nc))
                cluster.append([nr,nc])
    return cluster # 공중에 떠있다.

def drop(cluster, caven):
    while 1:
        cluster.sort(key=lambda x:x[0], reverse=True)
        cluster2 = []
        flag = 0
        for r,c in cluster:
            nr = r+1
            if nr >= R:
                flag = 1
                break
            else:
                if [nr, c] not in cluster:
                    if caven[nr][c] == 'x':
                        flag = 1
                        break
        if flag:
            break
        for r, c in cluster:
            caven[r+1][c] = caven[r][c]
            caven[r][c] = '.'
            cluster2.append([r+1, c])
        cluster = cluster2[:]
    return caven

R, C = map(int, input().split())
caven = [list(input().rstrip()) for _ in range(R)]
delta = ((0,1),(0,-1),(1,0),(-1,0))
N = int(input())
lst = list(map(int, input().split()))
turn = 1
for i in range(N):
    if turn == 1: # 왼쪽출발
        #caven[R-lst[i]] # 0행이 높이 R의 기준점
        flag = 0
        for j in range(C):
            if caven[R-lst[i]][j] == '.':  # 여기부터 확인    
                continue
            else:
                height = R-lst[i]
                caven[height][j] = '.' 
                for dr, dc in delta:
                    nr, nc = height+dr, dc+j
                    if 0 <= nr < R and 0 <= nc < C and caven[nr][nc] == 'x':
                        cluster = find(nr, nc)
                        if cluster:
                            caven2 = drop(cluster, caven)
                            caven = caven2[:]
                            flag = 1
                            break
                        else:
                            flag = 1
                # 부서진 미네랄 사방에 군집이 있는경우 그 군집들이 공중에 떠있는지 확인?
                # 공중에 떠있는 클러스터 확인후 어떻게 확인함? bfs돌려서 클러스터 찾고 클러스터의 최남단이 높이1인지(R-1행인지 확인하고 맞으면 떠있는게 아님?, 일단 두개이상 한번에 떨어지는 경우는 없기 때문에 공중에 떠있는거 확인하고 아래로 추락시키는 연산을 한번만 진행하면된다.)
                # 있으면 바닥으로 모양그대로 추락시킴
            if flag:
                break
    elif turn == -1: # 오른쪽출발
        for j in range(C-1,-1,-1):
            if caven[R-lst[i]][j] == '.':  # 여기부터 확인    
                continue
            else:
                height = R-lst[i]
                caven[height][j] = '.' 
                for dr, dc in delta:
                    nr, nc = height+dr, dc+j
                    if 0 <= nr < R and 0 <= nc < C and caven[nr][nc] == 'x':
                        cluster = find(nr, nc)
                        if cluster:
                            caven2 = drop(cluster, caven)
                            caven = caven2[:]
                            flag = 1
                            break
                        else:
                            flag = 1
            if flag:
                break
    
    turn *= -1

for i in caven:
    print(''.join(i))