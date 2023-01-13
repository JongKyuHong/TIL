import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
par = [[] for _ in range(N+1)]
for _ in range(N):
    a, b, c = map(int, input().split())
    if b != -1:
        par[b] = a
    if c != -1:
        par[c] = a
    tree[a].append((b,c))


root = 1
for i in range(1, N+1):
    if not par[i]:
        root = i
        break

lst = []
def dfs(root, level):
    for left, right in tree[root]:
        if left != -1:
            dfs(left, level+1)
        lst.append([root,level])
        if right != -1:
            dfs(right, level+1)

dfs(root, 1)
distance = [-1]*(N+1)
max_length = 0
max_level = 1
for i in range(len(lst)):
    node, level = lst[i]
    if distance[level] == -1:
        distance[level] = i
    else:
        if max_length == i-distance[level]:
            if max_level > level:
                max_level = level
        elif max_length < i-distance[level]:
            max_length = i-distance[level]
            max_level = level

print(max_level, max_length+1)