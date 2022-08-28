import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
lst = []

def dfs(start):
    if len(lst) == m:
        print(*lst)
        return
    for i in range(start, n):
        if nums[i] not in lst:
            lst.append(nums[i])
            dfs(i+1)
            lst.pop()


dfs(0)