import sys 
input = sys.stdin.readline
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]
dir = [[[0, -2], [1, -1], [-1, -1], [-2, 0], [2, 0], [-1, 0], [1, 0], [-1, 1], [1, 1], [0, -1]],
       [[2, 0], [1, -1], [1, 1], [0, -2], [0, 2], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, 0]],
       [[0, 2], [1, 1], [-1, 1], [-2, 0], [2, 0], [-1, 0], [1, 0], [-1, -1], [1, -1], [0, 1]],
       [[-2, 0], [-1, -1], [-1, 1], [0, -2], [0, 2], [0, -1], [0, 1], [1, -1], [1, 1], [-1, 0]]]
       
def rotate(r, c):
    global cnt
    while 1:
        for i in range(2):
            for _ in range(cnt):
                nr, nc = dr[i]+r, dc[i]+c
                spread(nr, nc, i)
                lst[r][c] = 0
                r, c = nr, nc
                if r == 0 and c == 0:
                    return
        cnt += 1
        for i in range(2, 4):
            for _ in range(cnt):
                nr, nc = dr[i]+r, dc[i]+c
                spread(nr, nc, i)
                r, c = nr, nc
        cnt += 1

def spread(r, c, d):
    global answer
    sand = lst[r][c]
    remain = sand
    for i in range(10):
        x, y = dir[d][i]
        if 0 <= x + r < N and 0 <= y + c < N:
            if i == 0:
                lst[x+r][y+c] += int(sand*0.05)
                remain -= int(sand*0.05)
            elif i == 1 or i == 2:
                lst[x+r][y+c] += int(sand*0.1)
                remain -= int(sand*0.1)
            elif i == 3 or i == 4:
                lst[x+r][y+c] += int(sand*0.02)
                remain -= int(sand*0.02)
            elif i == 5 or i == 6:
                lst[x+r][y+c] += int(sand*0.07)
                remain -= int(sand*0.07)
            elif i == 7 or i == 8:
                lst[x+r][y+c] += int(sand*0.01)
                remain -= int(sand*0.01)
            else:
                lst[x+r][y+c] += int(remain)
        else: # 밖으로 나간거?
            if i == 0:
                answer += int(sand*0.05)
                remain -= int(sand*0.05)
            elif i == 1 or i == 2:
                answer += int(sand*0.1)
                remain -= int(sand*0.1)
            elif i == 3 or i == 4:
                answer += int(sand*0.02)
                remain -= int(sand*0.02)
            elif i == 5 or i == 6:
                answer += int(sand*0.07)
                remain -= int(sand*0.07)
            elif i == 7 or i == 8:
                answer += int(sand*0.01)
                remain -= int(sand*0.01)
            else:
                answer += int(remain)

cnt = 1
answer = 0
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
rotate(N//2, N//2)
print(answer)