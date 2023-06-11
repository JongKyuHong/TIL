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
M = int(input())
parent = [i for i in range(N+1)]
for i in range(N):
    input_ = list(map(int, input().rstrip().split()))
    for j in range(N):
        if input_[j] != 0:
            if find(j+1) != find(i+1):
                union(j+1, i+1)

lst = list(map(int, input().rstrip().split()))
for i in range(M-1):
    flag = 0
    for j in range(i+1, M):
        if find(lst[i]) == find(lst[j]):
            flag = 1
            break
    if not flag:
        print("NO")
        exit()
print("YES")

# 반례
# 마지막에 탐색을 어떤식으로 진행해야하는가


