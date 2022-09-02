n  = int(input())

nums = list(range(1,n+1))
idx = 0
new_nums = []
while 1:
    if len(nums) == 1:
        print(nums[0])
        exit()
    if (idx+1) % 2 == 0:
        new_nums.append(nums[idx])
    if idx == len(nums)-1:
        nums = new_nums
        idx = 0
        new_nums = []
    idx += 1
 
