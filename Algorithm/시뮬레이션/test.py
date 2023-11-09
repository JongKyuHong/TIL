import sys 
input = sys.stdin.readline
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
visited = set()

for x, y, d, g in lst:
    x, y = y, x
    coordinate = [d]
    for i in range(g):
        cor = coordinate[::-1]
        for gg in cor:
            gg = (gg + 1)%4
            coordinate.append(gg)
    #print(coordinate)
    #visit = set()
    visited.add((x, y))
    #visit.add((x, y))
    for gg in coordinate:
        nr, nc = x+dr[gg], y+dc[gg]
        visited.add((nr, nc))
        #visit.add((nr, nc))
        x, y = nr, nc
answer = 0
for i in range(1, 101):
    for j in range(1, 101):
        if (i, j) in visited and (i-1, j) in visited and (i, j-1) in visited and (i-1, j-1) in visited:
            answer += 1
print(answer)