import sys
input = sys.stdin.readline

n = int(input()) # 굴다리의 길이
m = int(input()) # 가로등의 갯수
x = list(map(int, input().split()))

gap = 0

for i in range(m):
    if i == 0:
        gap = max(gap, x[i])
    else:
        if (x[i]-x[i-1])/2 > (x[i]-x[i-1])//2:
            print('hi')
            gap = max(gap, ((x[i]-x[i-1])//2)+1)
        else:
            print((x[i]-x[i-1])/2,'hi2')
            gap = max(gap, ((x[i]-x[i-1])//2))
gap = max(gap, n-x[-1])
print(gap)