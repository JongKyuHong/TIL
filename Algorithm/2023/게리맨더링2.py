import sys
input = sys.stdin.readline

def find(x, y, d1, d2):
    area = [[0]*(N+1) for _ in range(N+1)]
    area_val = [0 for i in range(6)]
    for i in range(d1 + 1):
        area[x + i][y - i] = 5
        area[x + d2 + i][y + d2 - i] = 5
    for i in range(d2 + 1):
        area[x + i][y + i] = 5
        area[x + d1 + i][y - d1 + i] = 5

    for r in range(1, x+d1):
        for c in range(1, y+1):
            if area[r][c] == 5:
                break
            else:
                area_val[1] += graph[r][c]
    
    for r in range(1, x+d2+1):
        for c in range(N, y, -1):
            if area[r][c] == 5:
                break
            else:
                area_val[2] += graph[r][c]
    
    for r in range(x+d1, N+1):
        for c in range(1, y-d1+d2):
            if area[r][c] == 5:
                break
            else:
                area_val[3] += graph[r][c]
    
    for r in range(x+d2+1, N+1):
        for c in range(N, y-d1+d2-1, -1):
            if area[r][c] == 5:
                break
            else:
                area_val[4] += graph[r][c]

    area_val[5] = total - sum(area_val)
    return max(area_val[1:]) - min(area_val[1:])
        
N = int(input())
graph = [[]]
for i in range(N):
    graph.append([0] + list(map(int, input().split())))

total = 0
for i in range(1, N + 1):
    total += sum(graph[i])
result = float('inf')
for x in range(1, N+1):
    for y in range(1, N+1):
        for d1 in range(1, N+1):
            for d2 in range(1, N+1):
                if 1 <= x < x + d1 + d2 <= N and 1 <= y - d1 < y < y + d2 <= N:
                    result = min(result, find(x,y,d1,d2))
print(result)
