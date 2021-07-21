def my_avg(*nums):
    sum = 0
    for i in nums:
        sum += i
    return sum/len(nums)

print(my_avg(77,83,95,80,70))