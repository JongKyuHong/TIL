import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
numbers = list(map(int, input().split())) # 덧셈, 뺄셈, 곱셈, 나눗셈의 갯수
ans_max, ans_min = -sys.maxsize, sys.maxsize

def dfs(idx, value):
    global ans_max, ans_min
    if idx == n:
        ans_max = max(value, ans_max)
        ans_min = min(value, ans_min)
        return
    for i in range(4):
        if i == 0 and numbers[i]:
            numbers[i] -= 1
            dfs(idx+1, value+nums[idx])
            numbers[i] += 1
        if i == 1 and numbers[i]:
            numbers[i] -= 1
            dfs(idx+1, value-nums[idx])
            numbers[i] += 1
        if i == 2 and numbers[i]:
            numbers[i] -= 1
            dfs(idx+1, value*nums[idx])
            numbers[i] += 1
        if i == 3 and numbers[i]:
            numbers[i] -= 1
            dfs(idx+1, int(value/nums[idx]))
            numbers[i] += 1


dfs(1, nums[0])
print(ans_max)
print(ans_min)


