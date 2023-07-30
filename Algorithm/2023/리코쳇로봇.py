from collections import deque
def solution(board):
    answer = float('inf')
    # 어떻게 진행 할 것인가 생각
    # 1. bfs를 이용할것인데 while문을 이용해서 갈수있는 가장 끝까지 이동시킴
    # 2. 방향은 늘 하던데로 delta로 선언
    # 3. 현재좌표랑 이동횟수를 q에 넣어서 판단
    # 4. 목표위치에 도달할 수 없는경우는 어떻게 판단할까??
    # 5. 같은 위치를 계속 돌면 도달할수없는 경우, 아까 도착한 위치를 다시 올 이유가 없으므로 도착한 지점은 visited에 저장해서 생각하자
    # 6. 5의 경우를 위해 dfs를 이용해야할것 같다.
    # 7. delta대신 그냥 반복문에서 판단
    N = len(board)
    M = len(board[0])
    q = deque()
    start_r, start_c = 0, 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                start_r, start_c = i, j
    
    visited = [[float('inf')]*M for _ in range(N)]
    visited[start_r][start_c] = 0
    q.append((start_r, start_c, 0))
    while q:
        r, c, cnt = q.popleft()
        if board[r][c] == 'G':
            return cnt
        for i in range(4):
            if i == 0: # 위
                nr = r
                while 0 <= nr-1 < N and board[nr-1][c] != 'D':
                    nr -= 1
                if visited[nr][c] > cnt+1:
                    visited[nr][c] = cnt+1
                    q.append((nr, c, cnt+1))
            elif i == 1: # 아래
                nr = r
                while 0 <= nr+1 < N and board[nr+1][c] != 'D':
                    nr += 1
                if visited[nr][c] > cnt+1:
                    visited[nr][c] = cnt+1
                    q.append((nr, c, cnt+1))
            elif i == 2: # 좌측
                nc = c
                while 0 <= nc-1 < M and board[r][nc-1] != 'D':
                    nc -= 1
                if visited[r][nc] > cnt+1:
                    visited[r][nc] = cnt+1
                    q.append((r, nc, cnt+1))
            else:
                nc = c
                while 0 <= nc+1 < M and board[r][nc+1] != 'D':
                    nc += 1
                if visited[r][nc] > cnt+1:
                    visited[r][nc] = cnt+1
                    q.append((r, nc, cnt+1))
                
    return answer if answer != float("inf") else -1