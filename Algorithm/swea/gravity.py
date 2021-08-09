t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int,input().split()))
    maxa = 0
    cnt = 0
    for i in range(n):
        for j in range(i+1,n):
            if array[i] > array[j]:
                cnt += 1
        maxa = max(maxa,cnt)
        cnt = 0
    print(maxa)



