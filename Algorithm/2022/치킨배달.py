import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

chicken = []
house = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            chicken.append([i, j])
        elif graph[i][j] == 1:
            house.append([i,j])

result = 9999999
for chi in combinations(chicken, M):
    tmp = 0
    for h in house:
        chi_len = 999
        for j in range(M):
            chi_len = min(chi_len, abs(h[0]-chi[j][0])+abs(h[1]-chi[j][1]))
        tmp += chi_len
    result = min(result, tmp)
print(result)