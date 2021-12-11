def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if b > a:
        parent[b] = a
    else:
        parent[a] = b

for test_case in range(int(input())):
    n, m = map(int, input().split())
    parent = [i for i in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        if find_parent(a) != find_parent(b):
            union_parent(a, b)
    res = []
    for i in range(1, n+1):
        pa = find_parent(i)
        if pa not in res:
            res.append(pa)
    print(f'#{test_case+1} {len(res)}')