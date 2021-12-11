def partition(left, right):
    if left >= right:
        return
    pivot = left
    i = left+1
    j = right-1
    while i <= j:
        while i <= j and array[pivot] >= array[i]:
            i += 1
        while i <= j and array[pivot] <= array[j]:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
    array[pivot], array[j] = array[j], array[pivot]
    partition(left, j)
    partition(j+1, right)


for test_case in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    left = 0
    right = len(array)
    partition(left, right)
    print(f'#{test_case+1} {array[n//2]}')