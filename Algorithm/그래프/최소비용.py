from collections import deque
move = [(1,0), (0,1), (-1,0), (0,-1)]


for test_case in range(int(input())):
    n = int(input())
    map_list = [list(map(int, input().split())) for _ in range(n)]
    INF = float('inf')
    distance = [[INF for _ in range(n)] for _ in range(n)]
    distance[0][0] = 0
    queue = deque()
    queue.append((0,0))
    while queue:
        y, x = queue.popleft()
        for dy, dx in move:
            my, mx = dy+y, dx+x
            if 0 <=my < n and 0 <= mx < n:
                temp = 1
                if map_list[my][mx] > map_list[y][x]:
                    temp += map_list[my][mx] - map_list[y][x]
                if distance[my][mx] > distance[y][x] + temp:
                    distance[my][mx] = distance[y][x] + temp
                    queue.append((my,mx))

    print(f'#{test_case+1} {distance[n-1][n-1]}')




