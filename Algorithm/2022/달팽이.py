n = int(input())
k = int(input())

nums = n**2
graph = [[0] * n for _ in range(n)]
r, c = 0, 0
graph[r][c] = nums
nums -= 1
while nums >= 1:
    dr = r + 1
    while 0 <= dr < n and not graph[dr][c]:
        graph[dr][c] = nums
        r = dr
        dr += 1
        nums -= 1
    dc = c + 1
    while 0 <= dc < n and not graph[r][dc]:
        graph[r][dc] = nums
        c = dc
        dc += 1
        nums -= 1
    dr = r - 1
    while 0 <= dr < n and not graph[dr][c]:
        graph[dr][c] = nums
        r = dr
        dr -= 1
        nums -= 1
    dc = c - 1
    while 0 <= dc < n and not graph[r][dc]:
        graph[r][dc] = nums
        c = dc
        dc -= 1
        nums -= 1

for i in graph:
    print(*i)

for i in range(n):
    for j in range(n):
        if graph[i][j] == k:
            print(i, j)



    
    

