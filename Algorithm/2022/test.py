n = int(input())
m = int(input())
array = list(map(int, input().split()))
array.sort()
cnt = 0

for i in range(n-1):
    ans = array[i]
    for j in range(i+1, n):
        if ans + array[j] == m:
            cnt += 1
            break
        elif ans + array[j] > m:
            break
        else:
            ans += array[j]
print(cnt)