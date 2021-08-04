n,l = map(int,input().split())
array = list(map(int,input().split()))
array.sort()
cnt = 0
tmp = 0
for p in array:
    if tmp < p:
        cnt += 1
        tmp = p+l-1
print(cnt)


    


