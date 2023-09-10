import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [list(input().rstrip()) for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(M):
        if lst[i][j] == '.':
            r, c = i, j
            flag = 0
            # r은 고정 c를 다봄
            for k in range(M):
                if lst[r][k] == 'X':
                    flag = 1
                    break
            if flag:
                continue
            flag = 0
            for k in range(N):
                if lst[k][c] == 'X':
                    flag = 1
                    break
            if flag:
                continue
            lst[i][j] = 'X'
            answer += 1

for i in range(N):
    for j in range(M):
        if lst[i][j] == '.':
            r, c = i, j
            flag = 0
            for k in range(M):
                if lst[r][k] == 'X':
                    flag = 1
                    break
            if not flag:
                lst[i][j] = 'X'
                answer += 1
                break
for j in range(M):
    for i in range(N):
        if lst[i][j] == '.':
            r, c = i, j
            flag = 0
            for k in range(N):
                if lst[k][c] == 'X':
                    flag = 1
                    break
            if not flag:
                lst[i][j] = 'X'
                answer += 1
                break
print(answer)