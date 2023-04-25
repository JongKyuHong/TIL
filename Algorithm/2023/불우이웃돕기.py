import sys
input = sys.stdin.readline

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
lst = [list(input().rstrip()) for _ in range(N)]
edge = []
total = 0
parent = [i for i in range(N+1)]
for i in range(N):
    for j in range(N):
        if lst[i][j] == 0:
            edge.append((0, i+1, j+1))
        else:
            if ord('a') <= ord(lst[i][j]) <= ord('z'):
                edge.append((ord(lst[i][j])-ord('a')+1, i+1, j+1))
                total += ord(lst[i][j]) - ord('a') + 1
            elif ord('A') <= ord(lst[i][j]) <= ord('Z'):
                edge.append((ord(lst[i][j])-ord('A')+27, i+1, j+1))
                total += ord(lst[i][j])-ord('A')+27

edge.sort(key=lambda x:x[0])
for value, x, y in edge:
    if value == 0:
        continue
    if find(x) != find(y):
        union(x, y)
        total -= value
check = set()
for i in range(1, N+1):
    if find(i) not in check:
        check.add(find(i))
if len(check) == 1:
    print(total)
else:
    print(-1)