import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

for case in range(1, int(input())+1):
    N = int(input())
    K = int(input())
    parent = [0]*(N)
    for i in range(N):
        parent[i] = i
    for _ in range(K):
        a, b = map(int, input().split())
        union(a, b)
    M = int(input())
    print(f'Scenario {case}:')
    for _ in range(M):
        a, b = map(int, input().split())
        if find(a) != find(b):
            print(0)
        else:
            print(1)
    print()