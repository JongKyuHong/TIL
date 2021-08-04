n,l = list(map(int,input().split()))
array = list(map(int,input().split()))
array.sort()
for i in array:
    if l >= i:
        l += 1
print(l)
