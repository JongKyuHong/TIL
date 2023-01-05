import sys
input = sys.stdin.readline

K = int(input())
lst = list(map(int, input().split()))
tree = [[] for _ in range(K)]

def makeTree(arr, n):
    if n >= K:
        return
    mid = len(arr)//2
    tree[n].append(arr[mid])
    makeTree(arr[:mid],n+1)
    makeTree(arr[mid+1:],n+1)

makeTree(lst, 0)

for i in tree:
    print(*i)