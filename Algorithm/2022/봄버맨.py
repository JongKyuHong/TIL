import sys
input = sys.stdin.readline

r, c, n = map(int, input().split())

time = [[0]*c for _ in range(r)]
graph = [list(input().rstrip()) for _ in range(r)]
delta = ((0,1),(0,-1),(1,0),(-1,0))

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'O':
            time[i][j] += 1
n -= 1
if n == 0:
    for i in graph:
        for j in i:
            print(j, end='')
        print()
    exit()

while 1:
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'O':
                time[i][j] += 1
            elif graph[i][j] == '.':
                graph[i][j] = 'O'
                time[i][j] = 0

    for i in range(r):
        for j in range(c):
            if time[i][j] == 3:
                graph[i][j] = '.'
                for dr, dc in delta:
                    nr, nc = dr+i, dc+j
                    if 0 <= nr < r and 0 <= nc < c:
                        graph[nr][nc] = '.'

    for i in range(r):
        for j in range(c):
            if graph[i][j] == '.':
                time[i][j] = 0
    
    n -= 1
    if n == 0:
        for i in graph:
            for j in i:
                print(j, end='')
            print()
        exit()
    ## 3

    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'O':
                time[i][j] += 1
    
    for i in range(r):
        for j in range(c):
            if time[i][j] == 3:
                graph[i][j] = '.'
                for dr, dc in delta:
                    nr, nc = dr+i, dc+j
                    if 0 <= nr < r and 0 <= nc < c:
                        graph[nr][nc] = '.'
    
    for i in range(r):
        for j in range(c):
            if graph[i][j] == '.':
                time[i][j] = 0
    n -= 1
    if n == 0:
        for i in graph:
            for j in i:
                print(j, end='')
            print()
        exit()
    ## 4
                

                
            
                

