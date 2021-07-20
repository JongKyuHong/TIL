n,m,k = map(int,input().split())
nums = list(map(int,input().split()))
nums = sorted(nums,reverse=True)
count = 0
sum = 0
for i in range(m):
    if count == k:
        count = 0
        sum += nums[1]
    else:
        count += 1
        sum += nums[0]
print(sum)