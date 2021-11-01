import time
start = time.time()

def binary_search():
    start = 0
    end = n-1
    while start <= end:
        mid = (start+end)//2
        #print(mid)
        if array[mid] == mid:
            return mid
        elif array[mid] < mid:
            start = mid + 1
        else:
            end = mid - 1
    return -1

n = int(input())
array = list(map(int, input().split()))
print(binary_search(), time.time()-start)

# import time
# start = time.time()
# def binary_search(array, start, end):
#     if start > end:
#         return None
#     mid = (start+end) // 2
#     if array[mid] == mid:
#         return mid
#     elif array[mid] > mid:
#         return binary_search(array, start, mid - 1)
#     else:
#         return binary_search(array, mid+1, end)
# n = int(input())
# array = list(map(int, input().split()))

# index = binary_search(array,0,n-1)

# if index == None:
#     print(-1, time.time()-start)
# else:
#     print(index, time.time()-start)