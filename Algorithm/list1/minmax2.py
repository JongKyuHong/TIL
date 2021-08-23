t = int(input())

for test_case in range(1,t+1):
    n = int(input())
    nums = list(map(int,input().split()))
    nums.sort()
    res = nums[-1] - nums[0]
    print(f'#{test_case} {res}')