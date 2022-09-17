n = int(input())
s,e = 0, n
while s <= e:
    mid = (s+e)//2
    if mid ** 2 < n:
        s = mid + 1
    else:
        e = mid - 1
print(s)
