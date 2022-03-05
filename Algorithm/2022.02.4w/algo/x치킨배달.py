from collections import combinations

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

home = []
chicken = []
for i in range(n):
    for j in range(n):
        if array[i][j] == 1: home.append((i,j))
        elif array[i][j] == 2: chicken.append((i,j))
minv = float('inf')

for ch in combinations(chicken, m):
    sumv = 0
    for h in home:
        sumv += min([abs(h[0]-i[0]) + abs(h[1]-i[1]) for i in ch])
        if minv <= sumv: break
    if sumv < minv: minv = sumv
print(minv)