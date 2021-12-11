# c, r = map(int, input().split())
# k = int(input())
# graph = [[0]*c for _ in range(r)]

# if r * c < k :
#     print(0)
#     exit(0)

# dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
# x, y, dir = 0, r-1, 0
# num = 1

# while num != k:
#     graph[y][x] = num
#     nx = x + dx[dir]
#     ny = y + dy[dir]
#     if nx < 0 or ny < 0 or nx >= c or ny >= r or graph[ny][nx] != 0:
#         dir = (dir+1)%4
#         nx = x + dx[dir]
#         ny = y + dy[dir]
#     x, y, num = nx, ny, num+1
# print(f'{x+1} {r-y}')

c, r = map(int, input().split())
k = int(input())

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
graph = [[0]*c for _ in range(r)]
x = 0
y = r-1
i = 0
num = 1
if r*c < k:
    print(0)
    exit(0)

while num != k:
    graph[y][x] = num
    nx = dx[i] + x
    ny = dy[i] + y
    if nx < 0 or ny < 0 or nx >= c or ny >= r or graph[ny][nx] != 0:
        i = (i+1)%4
        nx = x + dx[i]
        ny = y + dy[i]
    x, y = nx, ny
    num += 1

print(f'{x+1} {r-y}')