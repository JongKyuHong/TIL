import sys
from itertools import combinations
input = sys.stdin.readline


n, m = map(int, input().split()) # 고리 회원수, 치킨 종류의 수
graph = [list(map(int, input().split())) for _ in range(n)]
max_v = 0
for i in range(m): # 선택 치킨1
    for j in range(i+1, m): # 선택 치킨2
        for k in range(j+1, m): # 선택 치킨3
            res = 0
            for l in range(n):
                res += max(graph[l][i], graph[l][j], graph[l][k])
            max_v = max(max_v, res)
print(max_v)