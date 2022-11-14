import sys
input = sys.stdin.readline

m, n = map(int, input().split())
r, c, dir = 0, 0, 0
delta = ((0,1),(-1,0),(0,-1),(1,0))
for _ in range(n):
    a, b = input().rstrip().split()
    if a == 'MOVE':
        r += delta[dir][0]*int(b)
        c += delta[dir][1]*int(b)
        if r < 0 or r > m or c < 0 or c > m:
            print(-1)
            exit()
    else:
        if b == '1':
            dir += 1
            dir %= 4
        else:
            dir -= 1
            dir %= 4
print(c, r)