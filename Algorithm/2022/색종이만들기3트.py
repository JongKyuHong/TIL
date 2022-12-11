import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
blue, white = 0, 0
def check(r, c, n):
    global blue, white
    standard = graph[r][c]
    for i in range(r, r+n):
        for j in range(c, c+n):
            if graph[i][j] != standard:
                check(r, c, n//2)
                check(r+n//2, c, n//2)
                check(r, c+n//2, n//2)
                check(r+n//2, c+n//2, n//2)
                return
    if standard == 0:
        white += 1
    else:
        blue += 1

check(0, 0, n)
print(white)
print(blue)