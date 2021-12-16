from collections import deque

def solution(places):
    answer = []
    for i in places:
        flag = 1
        for a in range(5):
            for b in range(5):
                if i[a][b] == 'P':
                    result = bfs(i,a,b)
                    if not result:
                        flag = 0
        answer.append(flag)
    return answer

def bfs(graph, r, c):
    q = deque()
    visited = [[0]*5 for _ in range(5)]
    visited[r][c] = 1
    q.append((r,c,0))
    delta = ((0,1),(0,-1),(1,0),(-1,0))
    while q:
        r, c, d = q.popleft()
        for dr, dc in delta:
            nr = dr + r
            nc = dc + c
            nd = d + 1
            if 0 <= nr < 5 and 0 <= nc < 5 and not visited[nr][nc]:
                visited[nr][nc] = 1
                if graph[nr][nc] == 'P':
                    if nd <= 2:
                        return 0
                elif graph[nr][nc] == 'O':
                    if nd == 1:
                        q.append((nr,nc,nd))
    return 1
print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))