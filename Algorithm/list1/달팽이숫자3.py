t = int(input())

for test_case in range(1,t+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    row = [1,0,-1,0]
    col = [0,1,0,-1]
    x, y, step = 0, 0, 0
    for i in range(1,n**2):
        arr[x][y] = i
        x += row[step]
        y += col[step]
        if x < 0 or y < 0 or x >= n or y >= n or arr[x][y]:
            x -= row[step]
            y -= col[step]
            step = (step+1)%4
            x += row[step]
            y += row[step]
    print(f'#{test_case}')
    for i in arr:
        print(*i)







