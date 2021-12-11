# 최소 신장 트리 알고리즘
# 1. 간선 데이터를 비용에 따라 오름차순 정렬
# 2. 간선에 사이클이 발생하는지 확인한다.
# 2-1. 사이클이 발생하지 않으면 최소 신장트리에 포함
# 2-2. 사이클이 발생하는 경우 최소 신장트리에 포함시키지 않는다.
# 모든 간선에 대하여 2번과정 반복
# 간선의 갯수가 E일때 O(ElogE)의 시간 복잡도를 가진다.
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int, input().split())
parent = [0] * (v+1)
edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)        