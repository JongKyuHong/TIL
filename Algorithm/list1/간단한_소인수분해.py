t = int(input())

for test_case in range(1,t+1):
    n = int(input())
    nums = [2,3,5,7,11]
    res = [0]*5
    for i in range(len(nums)):
        while n%nums[i] == 0:
            res[i] += 1
            n //= nums[i]
    print(f'#{test_case}', *res)







