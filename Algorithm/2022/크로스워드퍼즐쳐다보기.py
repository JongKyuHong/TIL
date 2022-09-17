import sys
input = sys.stdin.readline

r, c = map(int, input().split())
graph = [input().rstrip() for _ in range(r)]
res = []
for i in range(r):
    ans = ''
    for j in range(c):
        if graph[i][j] != '#':
            ans += graph[i][j]
        else:
            if len(ans) >= 2:
                res.append(ans)
            ans = ''
    if len(ans) >= 2:
        res.append(ans)       

for i in range(c):
    ans = ''
    for j in range(r):
        if graph[j][i] != '#':
            ans += graph[j][i]
        else:
            if len(ans) >= 2:
                res.append(ans)
            ans = ''
    if len(ans) >= 2:
        res.append(ans)
res.sort()
print(res[0])