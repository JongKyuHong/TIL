def binary_search(array, target):
    start = 0
    end = len(array)-1
    while start <= end:
        mid = (start + end) //2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0
        
        
    

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
m = int(input())
nums2 = list(map(int, input().split()))
result = []
for target in nums2:
    print(binary_search(nums,target),end=' ')