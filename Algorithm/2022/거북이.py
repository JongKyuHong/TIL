import sys 
input = sys.stdin.readline

for _ in range(int(input())):
    movement = input().rstrip()
    r, c = 0, 0
    dir = 0 # 북
    delta = ((0,1),(1,0),(0,-1),(-1,0)) # 북 동 남 서
    max_r, min_r, max_c, min_c = 0, 0, 0, 0
    for move in movement:
        if move == 'F':
            dr, dc = delta[dir]
            r += dr
            c += dc
        elif move == 'B':
            dr, dc = delta[dir]
            r -= dr
            c -= dc
        elif move == 'L':
            dir -= 1
        else:
            dir += 1

        dir %= 4
        max_r = max(max_r, r)
        max_c = max(max_c, c)
        min_r = min(min_r, r)
        min_c = min(min_c, c)
    #print(max_r, max_c, min_r, min_c)
    print((max_r - min_r) * (max_c - min_c))
