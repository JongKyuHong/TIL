import sys
input = sys.stdin.readline

n, m = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(n)]
delta = ((0,1),(1,0))
ans = 2*m*n
visited = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        target = blocks[i][j]
        for dr, dc in delta:
            if 0 <= dr + i < n and 0 <= dc+j < m:
                if blocks[dr+i][dc+j] > target:
                    ans += blocks[dr+i][dc+j] - target
                else:
                    ans += target - blocks[dr+i][dc+j]

for i in range(m):
    ans += blocks[0][i]
for i in range(m):
    ans += blocks[-1][i]
for i in range(n):
    ans += blocks[i][0]
for i in range(n):
    ans += blocks[i][-1]

print(ans)                    