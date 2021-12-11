def divide(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)
    left = divide(arr[:mid//2])
    right = divide(arr[mid//2:])
    return merge(left, right)

def merge(left, right):
    global cnt
    left_l = len(left)
    right_l = len(right)
    result = [0]*(left_l+right_l)
    if left[-1] > right[-1]:
        cnt += 1

    left_i, right_i, i = 0, 0, 0
    while left_i < left_l or right_i < right_l:
        if left_i < left_l and right_i < right_l:
            if left[left_i] <= right[right_i]:
                result[i] = left[left_i]
                i += 1
                left_i += 1
            else:
                result[i] = right[right_i]
                i += 1
                right_i += 1
        elif left_i < left_l:
            result[i] = left[left_i]
            i += 1
            left_i += 1
        elif right_i < right_l:
            result[i] = right[right_i]
            i += 1
            right_i += 1
    return result



for test_case in range(int(input())):
    n = int(input())
    cnt = 0
    array = list(map(int,input().split()))
    res = divide(array)
    print(f'#{test_case+1} {res[n//2]} {cnt}')
