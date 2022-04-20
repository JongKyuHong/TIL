n = int(input())
a = list(map(int, input().split()))
b = [0] * n

def mergesort(a, low, high, b):
    if low >= high:
        return
    mid = (low+high)//2
    
    mergesort(a, low, mid, b)
    mergesort(a,mid+1, high,b)
    
    i = low
    j = mid + 1
    for k in range(low, high+1):
        if j > high:
            b[k] = a[i]
            i += 1
        elif i > mid:
            b[k] = a[j]
            j += 1
        elif a[i] <= a[j]:
            b[k] = a[i] 
            i += 1
        else:
            b[k] = a[j]
            j += 1
                 
    for l in range(low, high):
        a[l] = b[l]

    for num in a:
        print(num, end=" ")
    print()
mergesort(a,0,n-1,b)