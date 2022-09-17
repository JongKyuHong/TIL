def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

for _ in range(int(input())):
    nums = list(map(int, input().split()))
    num = nums[0]
    nums = nums[1:]
    res = 0
    for i in range(num):
        for j in range(i+1, num):
            if nums[i] < nums[j]:
                res += gcd(nums[i], nums[j])
            else:
                res += gcd(nums[j], nums[i])
    print(res)

