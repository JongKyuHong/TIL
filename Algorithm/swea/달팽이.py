t = int(input())


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for test_case in range(1,t+1):
    n = int(input())
    array = [[map(int,input().split())] for _ in range(n)]
    r, c = 0, 0
    dist = 0

    for n in range(1,(n**2)+1):
        array[r][c] = n 
        r += dr[dist]
        c += dc[dist]

        if r < 0 or c < 0 or c >= n or r >= n or array[r][c] !=0:
            r -= dr[dist]
            c -= dc[dist]
            dist = (dist+1)%4
            r += dr[dist]
            c += dc[dist]

    print(f'#{test_case}')
    for row in array:
        print(*row)
'''
    9 20 2 18 11
    19 1 25 3 21
    8 24 10 17 7
    15 4 16 5 6
    12 13 22 23 14
'''