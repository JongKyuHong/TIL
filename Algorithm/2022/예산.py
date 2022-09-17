n = int(input())
array = list(map(int, input().split()))
m = int(input())

start = 1
end = max(array)
ans = 0
while start <= end:
    mid = (start+end)//2
    target = 0
    for i in array:
        if mid > i:
            target += i
        else:
            target += mid
    
    if target > m:
        end = mid - 1
    elif target <= m:
        start = mid + 1 
        ans = max(ans, mid)

print(ans)