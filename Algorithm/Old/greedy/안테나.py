n = int(input())
home = list(map(int,input().split()))
home.sort()
h1 = home[n//2]

if n % 2==0:
    h2 = home[(n//2)-1]
    h1_sum = 0
    h2_sum = 0
    for i in range(n):
        h1_sum += abs(h1-home[i])
        h2_sum += abs(h2-home[i])
    if h1_sum < h2_sum:
        print(h1)
    else:
        print(h2)
else:
    print(h1)

