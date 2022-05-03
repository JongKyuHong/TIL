def quicksort(a, low, high):
    if low<high:
        pivot = a[high]
        i = low-1
        for j in range(low, high):
            if a[j] < pivot:
                i += 1
                a[i],a[j] = a[j], a[i]
        i += 1
        a[i], a[high] = a[high], a[i]
        for num in a:
            print(num, end=" ")
        print()
        
        quicksort(a, low, i-1)
        quicksort(a, i+1, high)

n = int(input())
nums = list(map(int, input().split()))
quicksort(nums, 0, n-1)
        