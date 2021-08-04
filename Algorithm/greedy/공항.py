import sys
from collections import deque
g = int(sys.stdin.readline())
p = int(sys.stdin.readline())
g1 = [int(sys.stdin.readline()) for _ in range(p)]

def parent_find(x):
    if x == parent[x]:
        return x
    p = parent_find(parent[x])
    parent[x] = p
    return parent[x]
def union(x,y):
    x = parent_find(x)
    y = parent_find(y)
    parent[x] = y

parent = {i:i for i in range(g+1)}

cnt = 0
for i in g1:
    x = parent_find(i)
    if x == 0:
        break
    union(x,x-1)
    cnt += 1
print(cnt)


        

    



