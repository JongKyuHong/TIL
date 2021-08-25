def quick_sort(left, right):
    if left >= right:
        return
    pivot = left
    i = left + 1
    j = right - 1
    while i <= j:
        while i <= j and array[pivot] >= array[i]: i += 1
        while i <= j and array[pivot] <= array[j]: j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
    array[pivot], array[j] = array[j], array[pivot]

    quick_sort(left, j)
    quick_sort(j+1, right)


for test_case in range(int(input())):
    n = int(input())
    array = list(map(int,input().split()))
    start = 0
    end = n
    quick_sort(start, n)
    print(f'#{test_case+1} {array[n//2]}')