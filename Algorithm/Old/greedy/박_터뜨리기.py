n,k = map(int,input().split())

target = 0
target2 = n%k
for i in range(1,k+1):
    target += i
if n < target:
    print(-1)
    exit(0)
elif n == target:
    print(k-1)
    exit(0)
else:
    if (n-target)%k in range(1,k):
        print(k)  # 맨위부터 맨아래 바로 전까지 
    else:
        print(k-1)  # 맨아래도 채워졌을때