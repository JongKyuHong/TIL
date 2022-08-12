k, n = map(int, input().split())
array = [int(input()) for _ in range(k)]

start = 1
end = max(array)
ans = 0
while start <= end:
    mid = (start+end)//2
    target = 0
    for i in array:
        target += i//mid
    if target < n:
        end = mid - 1
    elif target >= n:
        start = mid + 1
        ans = max(ans, mid)
print(ans)