def shoot(n):
    for index in range(w):
        explosion(index)
        gravity()
        shoot(n-1)

def explosion(c):
    for i in range(h):
        if bricks[i][c]:
            if bricks[i][c] == 1:
                bricks[i][c] = 0
                return
            else:
                ex_r = bricks[i][c]
                destroy(i, c, ex_r)
                return


def destroy(r, c, ex_r):
    cnt = ex_r-1
    while cnt > 0 and r > h:
        destroy_c(r, c, bricks[r][c])
        if bricks[r][c] > cnt:
            cnt = bricks[r][c]
        cnt -= 1
        r += 1


def destroy_c(r ,c, ex_r):
    if r-ex_r//2 >= 0 and r+ex_r < w:
        for i in range(r-ex_r//2, r+ex_r//2,1):
            bricks[r][i] = 0
    elif r-ex_r//2 < 0:
        for i in range(0, r+ex_r//2,1):
            bricks[r][i] = 0
    elif r+ex_r//2 >= w:
        for i in range(r-ex_r//2, n-1,1):
            bricks[r][i] = 0


def gravity():
    new_bricks = [[0]*w for _ in range(h)]
    new_bricks_index = h-1
    for i in range(w):
        for j in range(h-1,-1,-1):
            if bricks[j][i]:
                new_bricks[new_bricks_index][i] = bricks[j][i]
                new_bricks_index -= 1

            
            
for test_case in range(int(input())):
    n, w, h = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(h)]
    shoot(n)

