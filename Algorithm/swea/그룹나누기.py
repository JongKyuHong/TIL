def get_parent(x):
    if parent[x] != x:
        parent[x] = get_parent(parent[x])
    return parent[x]


def union_parent(x, y):
    a = get_parent(x)
    b = get_parent(y)
    if a > b:
        parent[a] = bs
    else:
        parent[b] = a


for t in range(int(input())):
    n, m = map(int, input().split())
    parent = [i for i in range(n+1)]
    votes = list(map(int, input().split()))
    for i in range(0, m*2, 2):
        union_parent(votes[i], votes[i+1])
    ans = set()
    for i in parent:
        ans.add(get_parent(i))
    print(f'#{t+1} {len(ans)-1}')
