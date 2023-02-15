from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N = int(input())
names = list(input().rstrip().split())
names.sort()
M = int(input())
parent = defaultdict(list)
root = {}
visited = {}
for i in range(N):
    visited[names[i]] = 0
for _ in range(M):
    X, Y = input().rstrip().split()
    parent[Y].append(X)
for k, v in parent.items():
    for j in v:
        visited[j] += 1

ans = []
for k, v in visited.items():
    if v == 0:
        ans.append(k)
print(len(ans))
print(*ans)
for i in range(N):
    lst = []
    for child in parent[names[i]]:
        if visited[child] == visited[names[i]] + 1:
            lst.append(child)
    lst.sort()
    print(names[i], len(lst), *lst)

