def buble(arr):  # On**2
    for i in range(len(arr)-1,0,-1):
        for j in range(0,i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

print(buble([9,4,5,6,1,2,7,3,8]))