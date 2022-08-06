n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

for _ in range(m):
    a, b = map(int, input().split())
    res = 0
    start, end = 0, n-1
    while start <= end:
        mid = (start+end) // 2
        if a > nums[mid]:
            start = mid + 1
        else:
            end = mid - 1
    startIdx = start
    start,end = 0, n-1
    while start <= end:
        mid = (start+end) // 2
        if nums[mid] > b:
            end = mid - 1
        else:
            start = mid + 1
    endIdx = end+1
    print(endIdx-startIdx)