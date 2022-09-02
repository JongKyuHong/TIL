import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()
left, right = 0, trees[-1]
max_v, target = 0, 0

while left <= right:
    mid = (left+right)//2
    val = 0
    for tree in trees:
        if mid < tree:
            val += tree-mid
    if val >= m:
        if target < mid:
            target = mid
        left = mid + 1
    else:
        right = mid - 1

print(target)
