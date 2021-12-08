for test_case in range(int(input())):
    n, k = map(int, input().split())
    a = n//4
    nums = input()
    numbers = []
    for _ in range(a):
        for i in range(0,len(nums),a):
            numbers.append(int(nums[i:i+a],16))
        nums = nums[-1] + nums[:len(nums)-1]
    numbers = list(set(numbers))
    numbers.sort(reverse=True)
    print(numbers[k-1])
    
    