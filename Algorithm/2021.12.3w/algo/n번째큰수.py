for _ in range(int(input())):
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    print(nums[2])