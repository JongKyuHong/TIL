import sys
input = sys.stdin.readline

N = int(input())
coordinate = [0, 0]*(N+1)
dist = 0
r, c = 0, 0
for i in range(1,N+1):
    x, y = map(int, input().split())
    coordinate[i] = [x, y]
    if i == 1:
        r, c = x, y
    else:
        dist += abs(r-x) + abs(c-y)
        r, c = x, y

ans = dist
for i in range(2, N):
    #coordinate[i][0], coordinate[i][1] # 이거 빼야됨
    cost = dist
    cost -= (abs(coordinate[i][0] - coordinate[i-1][0]) + abs(coordinate[i][1] - coordinate[i-1][1]))
    cost -= (abs(coordinate[i+1][0] - coordinate[i][0]) + abs(coordinate[i+1][1] - coordinate[i][1]))
    cost += (abs(coordinate[i+1][0]-coordinate[i-1][0]) + abs(coordinate[i+1][1] - coordinate[i-1][1]))
    ans = min(ans, cost)
print(ans)