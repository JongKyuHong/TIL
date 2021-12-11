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


v, e = map(int, input().split())
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i


cycle = False



for i in range(e):
    a, b = map(int, input().split())
    if get_parent(parent, a) == get_parent(parent, b):
        cycle = True
        print('사이클 발생')
        exit()
    else:
        union_parent(parent, a, b)

print('각 원소가 속한 집합: ', end='')
for i in range(1, v+1):
    print(get_parent(parent, i), end=' ')
print()

print('부모 테이블: ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')