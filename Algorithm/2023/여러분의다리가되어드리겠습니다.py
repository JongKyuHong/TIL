from collections import deque
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

N = int(input())
parent = [i for i in range(N+1)]

for _ in range(N-2):
    a, b = map(int, input().split())
    union(a, b)

answer = []
for i in range(1, N+1):
    if i == parent[i]:
        answer.append(i)
print(*answer)