from collections import deque
import sys
input = sys.stdin.readline

def bfs(r, c, br, bc):
    global ans
    q = deque()
    q.append((r, c, br, bc, 0))
    while q:
        r, c, br, bc, cnt = q.popleft()
        if cnt == 11:
            continue
        if cnt > ans:
            continue
        for i in range(4):
            if i == 0: # 아래로 옮길때
                nr, bnr = r, br
                flag = 0
                rflag = 0
                if nr > bnr: # 아래로 옮기는데 R이 더 아래에 있는경우
                    while 1:
                        nr += 1
                        if not 0 <= nr < N:
                            nr -= 1
                            break
                        if lst[nr][c] == '#':
                            nr -= 1
                            break
                        elif lst[nr][c] == 'O':
                            rflag = 1
                            break
                    while 1:
                        bnr += 1
                        if not 0 <= bnr < N:
                            bnr -= 1
                            break
                        if lst[bnr][bc] == '#':
                            bnr -= 1
                            break
                        elif (nr == bnr and c == bc):
                            if lst[bnr][bc] == 'O':
                                flag = 1
                            else:
                                bnr -= 1
                            break
                        elif lst[bnr][bc] == 'O': # 파란색 구슬이 먼저 구멍에 들어가는 경우 q에 넣지않음
                            flag = 1
                            break
                elif nr <= bnr: # 아래로 옮기는데 B가 더 아래에 있는 경우
                    while 1:
                        bnr += 1
                        if not 0 <= bnr < N:
                            bnr -= 1
                            break
                        if lst[bnr][bc] == '#':
                            bnr -= 1
                            break
                        elif lst[bnr][bc] == 'O': # 파란색 구슬이 먼저 구멍에 들어가는 경우 q에 넣지않음
                            flag = 1
                            break
                    while 1:
                        nr += 1
                        if not 0 <= nr < N:
                            nr -= 1
                            break
                        if lst[nr][c] == '#':
                            nr -= 1
                            break
                        elif (nr == bnr and c == bc):
                            if lst[nr][c] == 'O':
                                flag = 1
                            else:
                                nr -= 1
                            break
                        elif lst[nr][c] == 'O':
                            rflag = 1
                            break
                if not flag:
                    if rflag:
                        ans = min(ans, cnt+1)
                    else:
                        q.append((nr, c, bnr, bc, cnt+1))
            elif i == 1: # 위로 옮길때
                nr, bnr = r, br
                flag = 0
                rflag = 0
                if nr > bnr:
                    while 1:
                        bnr -= 1
                        if not 0 <= bnr < N:
                            bnr += 1
                            break
                        if lst[bnr][bc] == '#':
                            bnr += 1
                            break
                        elif lst[bnr][bc] == 'O': # 파란색 구슬이 먼저 구멍에 들어가는 경우 q에 넣지않음
                            flag = 1
                            break
                    while 1:
                        nr -= 1
                        if not 0 <= nr < N:
                            nr += 1
                            break
                        if lst[nr][c] == '#':
                            nr += 1
                            break
                        elif (nr == bnr and c == bc):
                            if lst[nr][c] == 'O':
                                flag = 1
                            else:
                                nr += 1
                            break
                        elif lst[nr][c] == 'O':
                            rflag = 1
                            break
                elif nr <= bnr:
                    while 1:
                        nr -= 1
                        if not 0 <= nr < N:
                            nr += 1
                            break
                        if lst[nr][c] == '#':
                            nr += 1
                            break
                        elif lst[nr][c] == 'O':
                            rflag = 1
                            break
                    while 1:
                        bnr -= 1
                        if not 0 <= bnr < N:
                            bnr += 1
                            break
                        if lst[bnr][bc] == '#':
                            bnr += 1
                            break
                        elif (nr == bnr and c == bc):
                            if lst[bnr][bc] == 'O':
                                flag = 1
                            else:
                                bnr += 1
                            break
                        elif lst[bnr][bc] == 'O': # 파란색 구슬이 먼저 구멍에 들어가는 경우 q에 넣지않음
                            flag = 1
                            break
                if not flag:
                    if rflag:
                        ans = min(ans, cnt+1)
                    else:
                        q.append((nr, c, bnr, bc, cnt+1))
            elif i == 2: # 왼쪽
                nc, bnc = c, bc
                flag = 0
                rflag = 0
                if nc > bnc: # R이 더 오른쪽에 있는경우
                    while 1:
                        bnc -= 1
                        if not 0 <= bnc < M:
                            bnc += 1
                            break
                        if lst[br][bnc] == '#':
                            bnc += 1
                            break
                        elif lst[br][bnc] == 'O': # B가 더 먼저 들어감
                            flag = 1
                            break
                    while 1:
                        nc -= 1
                        if not 0 <= nc < M:
                            nc += 1
                            break
                        if lst[r][nc] == '#':
                            nc += 1
                            break
                        elif lst[r][nc] == 'O':
                            rflag = 1
                            break
                        elif (nc == bnc and r == br):
                            if lst[r][nc] == 'O':
                                flag = 1
                            else:
                                nc += 1
                            break
                else:
                    while 1:
                        nc -= 1
                        if not 0 <= nc < M:
                            nc += 1
                            break
                        if lst[r][nc] == '#':
                            nc += 1
                            break
                        elif lst[r][nc] == 'O':
                            rflag = 1
                            break
                    while 1:
                        bnc -= 1
                        if not 0 <= bnc < M:
                            bnc += 1
                            break
                        if lst[br][bnc] == '#':
                            bnc += 1
                            break
                        elif lst[br][bnc] == 'O': # B가 더 먼저 들어감
                            flag = 1
                            break
                        elif (nc == bnc and r == br):
                            if lst[br][bnc] == 'O':
                                flag = 1
                            else:
                                bnc += 1
                            break
                if not flag:
                    if rflag:
                        ans = min(ans, cnt+1)
                    else:
                        q.append((r, nc, br, bnc, cnt+1))
            else:
                nc, bnc = c, bc
                flag = 0
                rflag = 0
                if nc > bnc: # 오른쪽으로 옮기는데 r이 더 오른쪽에 있다면
                    while 1:
                        nc += 1
                        if not 0 <= nc < M:
                            nc -= 1
                            break
                        if lst[r][nc] == '#':
                            nc -= 1
                            break
                        elif lst[r][nc] == 'O':
                            rflag = 1
                            break
                    while 1:
                        bnc += 1
                        if not 0 <= bnc < M:
                            bnc -= 1
                            break
                        if lst[br][bnc] == '#':
                            bnc -= 1
                            break
                        elif lst[br][bnc] == 'O': # B가 더 먼저 들어감
                            flag = 1
                            break
                        elif (nc == bnc and r == br):
                            if lst[br][bnc] == 'O':
                                flag = 1
                            else:
                                bnc -= 1
                            break
                else:
                    while 1:
                        bnc += 1
                        if not 0 <= bnc < M:
                            bnc -= 1
                            break
                        if lst[br][bnc] == '#':
                            bnc -= 1
                            break
                        elif lst[br][bnc] == 'O': # B가 더 먼저 들어감
                            flag = 1
                            break
                    while 1:
                        nc += 1
                        if not 0 <= nc < M:
                            nc -= 1
                            break
                        if lst[r][nc] == '#':
                            nc -= 1
                            break
                        elif lst[r][nc] == 'O':
                            rflag = 1
                            break
                        elif (nc == bnc and r == br):
                            if lst[r][nc] == 'O':
                                flag = 1
                            else:
                                nc -= 1
                            break
                if not flag:
                    if rflag:
                        ans = min(ans, cnt+1)
                    else:
                        q.append((r, nc, br, bnc, cnt+1))

N, M = map(int, input().split())
lst = [list(input().rstrip()) for _ in range(N)]
red_r, red_c, blue_r, blue_c = 0, 0, 0, 0
ans = 11
for i in range(N):
    for j in range(M):
        if lst[i][j] == 'R':
            red_r = i
            red_c = j
        elif lst[i][j] == 'B':
            blue_r = i
            blue_c = j

# 4가지 방향으로 모두 움직임
bfs(red_r, red_c, blue_r, blue_c)
print(ans if ans != 11 else -1)


# 하나씩 옮긴다. (동시에 옮겨야 하므로)
# r, br 누구 먼저 옮길것인지 대소와 방향에 따라 다르게 결정
# 옮겼는데 좌표가 같아진경우는 뒤에 옮긴친구를 롤백한다

# 한쪽방향으로 기울때는 갈수있는 최대한으로 가야함
# 돌아가면서 하나씩 옮김?
# 예시로 왼쪽에 B 오른쪽에 R이있을때 왼쪽으로 쏠리는경우 어떻게 판단할것인가
# 실제로 하나씩 옮기면서

