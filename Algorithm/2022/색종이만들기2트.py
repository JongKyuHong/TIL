import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
blue = 0
white = 0
def find(r, c, n):
    global blue, white
    standard = graph[r][c]
    for i in range(r, r+n):
        for j in range(c, c+n):
            if graph[i][j] != standard:
                find(r, c, n//2)
                find(r+n//2, c, n//2)
                find(r, c+n//2, n//2)
                find(r+n//2, c+n//2, n//2)
                return
    if standard == 1:
        blue +=1 
    else:
        white += 1
            
find(0, 0, n)
print(white)
print(blue)