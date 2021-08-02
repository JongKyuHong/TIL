n,m = map(int,input().split())
j = int(input())
apple = []
for _ in range(j):
    apple.append(int(input()))

cnt= 0
left = 1
right = m
for i in range(j):  # 처음부터 돈다 
    if left <= apple[i] <= right:
        continue
    else:
        if apple[i]>right:
            temp = apple[i]-right
            cnt += temp
            left += temp
            right += temp
        if apple[i]<left:
            temp = left - apple[i]
            cnt += temp
            left -= temp
            right -= temp
print(cnt)