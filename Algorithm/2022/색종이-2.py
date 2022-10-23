import sys
input = sys.stdin.readline

n = int(input()) # 색종이 수
graph = [[0]*100 for _ in range(100)]
for _ in range(n):
    b, a = map(int, input().split()) # 색종이 붙인 위치
    for i in range(99-a, 89-a, -1):
        for j in range(b, 10+b):
            graph[i][j] += 1
delta = ((0,1),(0,-1),(1,0),(-1,0))
answer = 0
idx = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 0:
            for dr, dc in delta:
                nr, nc = dr+i, dc+j
                if 0 <= nr < 100 and 0 <= nc < 100 and graph[nr][nc]:
                    answer += 1
        else:
            if i == 0 or i == 99 or j == 0 or j == 99:
                if (i == 0 and j == 0) or (i==99 and j == 99) or (i==0 and j==99) or (i==99 and j == 0):
                    answer += 2
                else:
                    answer += 1
print(answer)
