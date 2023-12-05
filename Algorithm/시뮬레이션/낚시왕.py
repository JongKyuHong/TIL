import sys 
input = sys.stdin.readline
dc = [0, 0, 1, -1]
dr = [-1, 1, 0, 0]


def find(c):
    global answer
    for i in range(R):
        if lst[i][c]:
            answer += lst[i][c][2]
            lst[i][c] = []
            return

def move_shark(r, c, s, d):
    global R, C
    # 나머지 연산으로 처리해야된다.
    # 속도는 남은 거리라고 보면 된다.
        # r을 s에 더해서 0부터 시작하는 느낌으로 간다?
    while s > 0:
        nr, nc = dr[d]+r, dc[d]+c
        if 0 > nr or nr >= R or 0 > nc or nc >= C:
            if d == 0 or d == 2:
                d += 1
            else:
                d -= 1
            continue
        r, c = nr, nc
        s -= 1
    return [r, c, d]

def move():
    global lst
    coordinate = set()

    for i in range(R):
        for j in range(C):
            if lst[i][j]:
                s, d, z = lst[i][j] # 속력, 방향, 크기
                r1, c1, d1 = move_shark(i, j, s, d)
                coordinate.add((r1, c1, s, d1, z))
                lst[i][j] = []

    # 상어 잡아먹기
    for r, c, s, d, z in coordinate: 
        if lst[r][c]:
            if lst[r][c][2] < z:
                lst[r][c] = [s, d, z]
        else:
            lst[r][c] = [s, d, z]
    
R, C, M = map(int, input().split())
lst = [[[] for _ in range(C)] for _ in range(R)]
answer = 0

for _ in range(M):  
    r, c, s, d, z = map(int, input().split())
    r -= 1; c -= 1; d -= 1
    lst[r][c] = [s, d, z]

r, c = 0, -1

while 1:
    # 첫번째 오른쪽 한칸이동
    c += 1 
    if c == C:
        break
    # 두번째 가장 가까운 상어 잡기
    find(c)
    # 세번째 상어 이동
    move()

print(answer)