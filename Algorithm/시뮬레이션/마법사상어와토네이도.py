import sys 
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
left = [
(-2, 0, 0.02), (-1, -1, 0.10), (-1, 0, 0.07),
(-1, 1, 0.01), (0, -2, 0.05), (1, -1, 0.10),
(1, 0, 0.07), (1, 1, 0.01), (2, 0, 0.02)
]
down = [(-y, x, val) for x, y, val in left] 
right = [(x, -y, val) for x, y, val in left]
up = [(y, x, val) for x, y, val in left]
ratio = [left, down, right, up]

def move():
    global r, c, dir, turned, moved, target
    if moved == target:
        moved = 0
        turned += 1
        dir = (dir+1) % 4
    if turned == 2:
        turned = 0
        target += 1
    r = r + dx[dir]
    c = c + dy[dir]
    moved += 1

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
r, c = N//2, N//2
dir = 0
turned = 0
moved = 0
target = 1
result = 0
cnt = 1

while cnt < N * N:
    move()
    remain = lst[r][c]
    for i in range(9):
        nr, nc, percentage = ratio[dir][i]
        nr += r
        nc += c
        current = int(lst[r][c] * percentage)
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            result += current
        else:
            lst[nr][nc] += current
        remain -= current
    nr = r + dx[dir]
    nc = c + dy[dir]
    if nr < 0 or nr >= N or nc < 0 or nc >= N:
        result += remain
    else:
        lst[nr][nc] += remain
    lst[r][c] = 0
    cnt += 1
print(result)





        

# 격자 밖으로 나간 모래 양을 구하라
# 좌표상으로 N//2, N//2 부터 시작
# 왼아오위 방향으로 2개를 거치며 1씩 커짐
