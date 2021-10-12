def go(r, c, direction):
    for i in range(direction, 4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nc < 0 or nc >= n or nr < 0 or nr >= n or graph[nr][nc] in de:
            continue
        de.append(graph[nr][nc])
        go(nr, nc, i)
        de.remove(graph[nr][nc])
    len_de = len(de)
    if start_r == nr and start_c == nc and len_de >= 4:
        global ans
        if ans < len_de:
            ans = len_de
    return


for test_case in range(int(input())):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    dr = [1, -1, -1, 1]
    dc = [1, 1, -1, -1]
    res = -1
    visited = [[0]*n for _ in range(n)]
    ans = -1
    for i in range(n):
        for j in range(n):
            de = [graph[i][j]]
            start_r = i
            start_c = j
            go(i, j, 0)
            if ans:
                if res < ans:
                    res = ans

    print(f'#{test_case+1} {res}')
