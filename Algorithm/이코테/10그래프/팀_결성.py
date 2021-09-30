def get_parent(parent, x):
    if parent[x] != x:
        parent[x] = get_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if b > a:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i


for _ in range(m):
    check, a, b = map(int, input().split())
    if check == 0:
        union_parent(parent, a, b)
    else:
        if get_parent(parent, a) == get_parent(parent, b):
            print('YES')
        else:
            print('NO')