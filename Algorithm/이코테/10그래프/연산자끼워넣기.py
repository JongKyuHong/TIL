def dfs(array,start,next):
    for i in range(4):
        if i == 0:
            res = nums[start] + nums[next]
        elif i == 1:
            res = nums[start] - nums[start]
        elif i == 2:
            res = nums[start] * nums[start]
        else:
            res = nums[start] / nums[start]
        dfs(array,start,next)


n = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))
res_min = float('inf')
res_max = 0

dfs(1, nums[0], op[0], op[1], op[2], op[3])


