import sys
input = sys.stdin.readline

T = int(input())

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        parent[b] = a 
        number[a] += number[b]

for _ in range(T):  
    F = int(input())
    parent = {}
    number = {}
    for _ in range(F):
        f1, f2 = input().rstrip().split()
        if f1 not in parent:
            parent[f1] = f1
            number[f1] = 1
        if f2 not in parent:
            parent[f2] = f2
            number[f2] = 1
        union(f1, f2)
        print(number[find(f1)])
        