for _ in range(10):
    tc = int(input())
    graph = [list(map(int,input().split())) for _ in range(100)]
    col = graph[99].index(2)
    row = 99
    while 1:
        while graph[row][col+1] == 0 and graph[row][col-1] == 0:
            row -= 1
        while graph[row][col+1] == 1:
            col += 1
        while graph[row][col-1] == 1:
            col -= 1
        if row == 0:
            break
    print(f'#{tc} {col}')