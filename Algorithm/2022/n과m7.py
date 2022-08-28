import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
lst = []
def dfs(cnt):
    if cnt == m:
        print(' '.join(map(str,lst)))
        return
    
    for i in range(n):
        lst.append(nums[i])
        dfs(cnt+1)
        lst.pop()


dfs(0)