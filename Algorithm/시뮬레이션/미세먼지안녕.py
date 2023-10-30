import sys 
input = sys.stdin.readline
delta = ((0,1),(0,-1),(1,0),(-1,0))


def diffusion():
    global lst
    tmp = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if lst[i][j] == -1:
                tmp[i][j] = -1
                continue
            remain = 0
            for dr, dc in delta:
                nr, nc = dr+i, dc+j
                if 0 <= nr < R and 0 <= nc < C and lst[nr][nc] != -1:
                    tmp[nr][nc] += (lst[i][j]//5)
                    remain += lst[i][j]//5
            tmp[i][j] += lst[i][j] - remain
    lst = tmp

def rotate(coordinate, dir):
    r, c = coordinate
    if dir == 'up': # 위로 도는 공기
        # down
        for i in range(r-1, 0, -1):
            lst[i][0] = lst[i-1][0]

        # <-
        for i in range(0, C-1):
            lst[0][i] = lst[0][i+1]

        # up
        for i in range(0, r):
            lst[i][C-1] = lst[i+1][C-1]
        # ->
        for i in range(C-1, 1, -1):
            lst[r][i] = lst[r][i-1]
        lst[r][1] = 0
    else: 
        # up
        for i in range(r+1, R-1):
            lst[i][0] = lst[i+1][0]

        # <- 
        for i in range(0, C-1):
            lst[R-1][i] = lst[R-1][i+1]
        # down
        for i in range(R-1, r, -1):
            lst[i][C-1] = lst[i-1][C-1]

        # ->
        for i in range(C-1, 1, -1):
            lst[r][i] = lst[r][i-1]
        lst[r][1] = 0

R, C, T = map(int, input().split())
cleaner = []
lst = []
dust = []
for i in range(R):
    tmp = list(map(int, input().split()))
    for j in range(C):
        if tmp[j] == -1 and not cleaner:
            cleaner = [[i, j], [i+1, j]]
        elif tmp[j] > 0:
            dust.append([i, j])
    lst.append(tmp)

# 모든 먼지가 한번에 확산되어야 한다.
# 변경값을 어떤곳에 저장해놓고?

time = 0
while 1:
    diffusion()
    time += 1
    rotate(cleaner[0],'up')
    rotate(cleaner[1],'down')
    if time == T:
        answer = 0
        for i in lst:
            answer += sum(i)
        print(answer + 2)
        break



