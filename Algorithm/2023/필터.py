import sys
input = sys.stdin.readline

def find(r, c):
    lst = []
    for i in range(r, r+3):
        for j in range(c, c+3):
            lst.append(graph[i][j])
    lst.sort()
    return lst[4]


R, C = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]
T = int(input())
tmp = []
for i in range(R-2):
    for j in range(C-2):
        tmp.append(find(i, j))

cnt = 0
for i in tmp:
    if i >= T:
        cnt += 1
print(cnt)