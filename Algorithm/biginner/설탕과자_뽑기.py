h, w = map(int,input().split())
n = int(input())
grid = [[0]*w for _ in range(h)]
for _ in range(n):
    l,d,x,y = map(int,input().split())
    for j in range(l):
        if d == 0:
            grid[x-1][y-1+j] = 1
        else:
            grid[x-1+j][y-1] = 1

for i in grid:
    for j in i:
        print(j, end=' ')
    print()
