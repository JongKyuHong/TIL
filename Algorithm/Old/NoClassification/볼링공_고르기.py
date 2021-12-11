n,m = map(int,input().split())
k = list(map(int,input().split()))
count = i = 0
while i <= len(k):
    for j in range(i,len(k)):
        if k[i] != k[j]:
            count += 1
    i += 1
print(count)
        




