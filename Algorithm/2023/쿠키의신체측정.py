import sys
input = sys.stdin.readline

N = int(input())
lst = [list(input().rstrip()) for _ in range(N)]
head = []
flag = 0
for i in range(N):
    for j in range(N):
        if lst[i][j] == '*':
            head.append((i, j))
            flag = 1
            break
    if flag:
        break
heart_r, heart_c = head[0][0] + 2, head[0][1] + 1 
left_arm, right_arm, left_leg, right_leg = 0, 0, 0, 0
waist = 0

r, c = head[0][0] + 1, head[0][1] # 심장
nc = c
while 0 <= nc < N:
    if lst[r][nc] == '*':
        nc -= 1
    else:
        left_arm = c - nc - 1
        break
else:
    left_arm = c - nc - 1
nc = c
while 0 <= nc < N:
    if lst[r][nc] == '*':
        nc += 1
    else:
        right_arm = nc - c - 1
        break
else:
    right_arm = nc - c - 1
nr = r
while 0 <= nr < N:
    if lst[nr][c] == '*':
        nr += 1
    else:
        waist = nr - r - 1
        break
nc = c
nr2 = nr
while 0 <= nr2 < N:
    if lst[nr2][c-1] == '*':
        nr2 += 1
    else:
        left_leg = nr2 - nr
        break
else:
    left_leg = nr2 - nr

nr2 = nr
while 0 <= nr2 < N:
    if lst[nr2][c+1] == '*':
        nr2 += 1
    else:
        right_leg = nr2 - nr
        break
else:
    right_leg = nr2 - nr

print(heart_r, heart_c)
print(left_arm, right_arm, waist, left_leg, right_leg)
