n = int(input())
nums = []
answer = 5
for i in range(n):
    nums.append(int(input()))
nums.sort()
for i in range(n):
    cnt = 0
    for j in range(nums[i], nums[i]+5):
        if j not in nums:
            cnt += 1
    answer = min(answer, cnt)
print(answer)