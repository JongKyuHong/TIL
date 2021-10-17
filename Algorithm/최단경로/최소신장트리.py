import heapq

def get_parent(x):
    if parents[x] != x:
        parents[x] = get_parent(parents[x])
    return parents[x]


def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)
    if b > a:
        parents[b] = a
    else:
        parents[a] = b
for test_case in range(int(input())):
    V, E = map(int, input().split())
    q = []
    parents = [i for i in range(V+1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        heapq.heappush(q,(w,n1,n2))
    
    ans = 0
    while q:
        w, n1, n2 = heapq.heappop(q)
        if get_parent(n1) != get_parent(n2):
            union_parent(n1, n2)
            ans += w
    print(f'#{test_case+1} {ans}')



