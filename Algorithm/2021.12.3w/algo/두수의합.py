n = int(input())
nums = list(map(int, input().split()))
nums.sort()
x = int(input())
start,end = 0, n-1
ans = 0
while start < end:
    tmp = nums[start] + nums[end]
    if tmp == x: ans += 1
    if tmp < x:
        start += 1
        continue
    end -= 1
print(ans)
    

