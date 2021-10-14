def get_parent(parent ,x):
    if parent[x] != x:
        get_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if b > a:
        parent[b] = a
    else:
        parent[a] = b


for test_case in range(int(input())):
    v, e = map(int, input().split())
    _list = [list(map(int, input().split())) for _ in range(e)]
    parent = [i for i in range(v+1)]
    ans = 0
    _list.sort()
    for edge in _list:
        n1, n2, w = edge
        if get_parent(parent, n1) != get_parent(parent, n2):
            union_parent(parent, n1, n2)
            ans += w
    print(ans)